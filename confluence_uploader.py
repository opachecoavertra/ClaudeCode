#!/usr/bin/env python3
"""
Confluence Page Uploader

This script uploads converted HTML content to Confluence using the REST API.
It can also upload images as attachments to the page.
"""

import requests
import os
import sys
from pathlib import Path
import json


class ConfluenceUploader:
    """Handles uploading content to Confluence via REST API"""

    def __init__(self, base_url, username, api_token):
        """
        Initialize the Confluence uploader

        Args:
            base_url: Confluence base URL (e.g., https://your-domain.atlassian.net)
            username: Your Confluence email/username
            api_token: Your Confluence API token
        """
        self.base_url = base_url.rstrip('/')
        self.auth = (username, api_token)
        self.headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_page_info(self, page_id):
        """Get current page information including version number"""
        url = f"{self.base_url}/rest/api/content/{page_id}"
        response = requests.get(url, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def create_page(self, space_key, title, html_content, parent_id=None):
        """
        Create a new Confluence page

        Args:
            space_key: The space key where to create the page
            title: Page title
            html_content: HTML content in Confluence Storage Format
            parent_id: Optional parent page ID

        Returns:
            dict: Created page information
        """
        url = f"{self.base_url}/rest/api/content"

        data = {
            "type": "page",
            "title": title,
            "space": {"key": space_key},
            "body": {
                "storage": {
                    "value": html_content,
                    "representation": "storage"
                }
            }
        }

        if parent_id:
            data["ancestors"] = [{"id": parent_id}]

        response = requests.post(url, json=data, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def update_page(self, page_id, title, html_content):
        """
        Update an existing Confluence page

        Args:
            page_id: The page ID to update
            title: New page title
            html_content: HTML content in Confluence Storage Format

        Returns:
            dict: Updated page information
        """
        # Get current page info to get the current version
        page_info = self.get_page_info(page_id)
        current_version = page_info['version']['number']

        url = f"{self.base_url}/rest/api/content/{page_id}"

        data = {
            "version": {"number": current_version + 1},
            "title": title,
            "type": "page",
            "body": {
                "storage": {
                    "value": html_content,
                    "representation": "storage"
                }
            }
        }

        response = requests.put(url, json=data, auth=self.auth, headers=self.headers)
        response.raise_for_status()
        return response.json()

    def upload_attachment(self, page_id, file_path, comment=""):
        """
        Upload a file as an attachment to a Confluence page

        Args:
            page_id: The page ID to attach to
            file_path: Path to the file to upload
            comment: Optional comment for the attachment

        Returns:
            dict: Attachment information
        """
        url = f"{self.base_url}/rest/api/content/{page_id}/child/attachment"

        # Check if attachment already exists and delete if so
        filename = os.path.basename(file_path)
        self._delete_attachment_if_exists(page_id, filename)

        # Upload new attachment
        files = {'file': (filename, open(file_path, 'rb'))}
        headers = {'X-Atlassian-Token': 'nocheck'}

        response = requests.post(
            url,
            files=files,
            headers=headers,
            auth=self.auth,
            data={'comment': comment}
        )
        response.raise_for_status()
        return response.json()

    def _delete_attachment_if_exists(self, page_id, filename):
        """Delete an attachment if it already exists"""
        url = f"{self.base_url}/rest/api/content/{page_id}/child/attachment"
        params = {'filename': filename}

        response = requests.get(url, params=params, auth=self.auth)
        if response.status_code == 200:
            results = response.json().get('results', [])
            if results:
                attachment_id = results[0]['id']
                delete_url = f"{self.base_url}/rest/api/content/{attachment_id}"
                requests.delete(delete_url, auth=self.auth)

    def upload_directory_attachments(self, page_id, directory_path):
        """
        Upload all files from a directory as attachments

        Args:
            page_id: The page ID to attach to
            directory_path: Path to the directory containing files

        Returns:
            list: List of uploaded attachment information
        """
        directory = Path(directory_path)
        results = []

        if not directory.exists() or not directory.is_dir():
            raise ValueError(f"Directory not found: {directory_path}")

        for file_path in directory.iterdir():
            if file_path.is_file():
                print(f"Uploading {file_path.name}...")
                try:
                    result = self.upload_attachment(page_id, str(file_path))
                    results.append(result)
                    print(f"  ✓ Uploaded {file_path.name}")
                except Exception as e:
                    print(f"  ✗ Failed to upload {file_path.name}: {e}")

        return results


def main():
    """Main function to run the uploader from command line"""
    import argparse

    parser = argparse.ArgumentParser(description='Upload content to Confluence')
    parser.add_argument('--url', required=True, help='Confluence base URL')
    parser.add_argument('--username', required=True, help='Confluence username/email')
    parser.add_argument('--token', required=True, help='Confluence API token')
    parser.add_argument('--page-id', help='Page ID to update (if updating existing page)')
    parser.add_argument('--space', help='Space key (if creating new page)')
    parser.add_argument('--title', required=True, help='Page title')
    parser.add_argument('--html-file', required=True, help='Path to HTML file')
    parser.add_argument('--images-dir', help='Directory containing images to upload as attachments')
    parser.add_argument('--parent-id', help='Parent page ID (if creating new page)')

    args = parser.parse_args()

    # Validate arguments
    if not args.page_id and not args.space:
        parser.error("Either --page-id (for update) or --space (for create) must be specified")

    # Read HTML content
    with open(args.html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Create uploader
    uploader = ConfluenceUploader(args.url, args.username, args.token)

    try:
        if args.page_id:
            # Update existing page
            print(f"Updating page {args.page_id}...")
            result = uploader.update_page(args.page_id, args.title, html_content)
            print(f"✓ Page updated successfully!")
            page_id = args.page_id
        else:
            # Create new page
            print(f"Creating new page in space {args.space}...")
            result = uploader.create_page(args.space, args.title, html_content, args.parent_id)
            print(f"✓ Page created successfully!")
            page_id = result['id']

        print(f"Page URL: {args.url}/pages/viewpage.action?pageId={page_id}")

        # Upload images if directory provided
        if args.images_dir:
            print(f"\nUploading images from {args.images_dir}...")
            uploader.upload_directory_attachments(page_id, args.images_dir)
            print("✓ Images uploaded successfully!")

    except requests.exceptions.HTTPError as e:
        print(f"✗ HTTP Error: {e}")
        print(f"Response: {e.response.text}")
        sys.exit(1)
    except Exception as e:
        print(f"✗ Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    # Example usage (can be run directly or imported as a module)
    if len(sys.argv) == 1:
        print("Confluence Uploader")
        print("==================")
        print()
        print("Usage:")
        print("  # Update existing page")
        print("  python3 confluence_uploader.py \\")
        print("    --url https://your-domain.atlassian.net \\")
        print("    --username your-email@example.com \\")
        print("    --token your-api-token \\")
        print("    --page-id 123456 \\")
        print("    --title 'My Page Title' \\")
        print("    --html-file confluence_output.html \\")
        print("    --images-dir extracted_docs/images")
        print()
        print("  # Create new page")
        print("  python3 confluence_uploader.py \\")
        print("    --url https://your-domain.atlassian.net \\")
        print("    --username your-email@example.com \\")
        print("    --token your-api-token \\")
        print("    --space MYSPACE \\")
        print("    --title 'My Page Title' \\")
        print("    --html-file confluence_output.html \\")
        print("    --images-dir extracted_docs/images \\")
        print("    --parent-id 123456")
        print()
        print("To get a Confluence API token:")
        print("  1. Go to https://id.atlassian.com/manage-profile/security/api-tokens")
        print("  2. Click 'Create API token'")
        print("  3. Give it a name and copy the token")
        sys.exit(0)
    else:
        main()
