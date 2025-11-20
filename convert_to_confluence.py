#!/usr/bin/env python3
"""
Google Docs to Confluence HTML Converter

This script converts Google Docs exported HTML to Confluence Storage Format.
"""

import re
import html
from html.parser import HTMLParser
from pathlib import Path
import sys


class GoogleDocsToConfluenceConverter(HTMLParser):
    """Converts Google Docs HTML to Confluence Storage Format"""

    def __init__(self):
        super().__init__()
        self.confluence_html = []
        self.in_body = False
        self.current_tag = None
        self.tag_stack = []
        self.list_stack = []
        self.skip_tags = {'style', 'script', 'head', 'meta'}
        self.current_attrs = {}
        self.image_counter = 0

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Skip unwanted tags
        if tag in self.skip_tags:
            self.tag_stack.append(('skip', None))
            return

        # Start body processing
        if tag == 'body':
            self.in_body = True
            self.tag_stack.append((tag, None))
            return

        if not self.in_body:
            self.tag_stack.append(('skip', None))
            return

        # Handle different HTML elements
        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            self.confluence_html.append(f'<{tag}>')
            self.tag_stack.append((tag, None))

        elif tag == 'p':
            # Check if it's an empty paragraph or has class
            self.confluence_html.append('<p>')
            self.tag_stack.append((tag, None))

        elif tag in ['strong', 'b']:
            self.confluence_html.append('<strong>')
            self.tag_stack.append(('strong', None))

        elif tag in ['em', 'i']:
            self.confluence_html.append('<em>')
            self.tag_stack.append(('em', None))

        elif tag == 'u':
            self.confluence_html.append('<u>')
            self.tag_stack.append((tag, None))

        elif tag == 'a':
            href = attrs_dict.get('href', '#')
            self.confluence_html.append(f'<ac:link><ri:url ri:value="{html.escape(href)}" /></ac:link>')
            self.tag_stack.append(('a_skip', None))

        elif tag == 'img':
            src = attrs_dict.get('src', '')
            # Handle embedded images
            if src.startswith('images/'):
                image_name = src.split('/')[-1]
                self.image_counter += 1
                self.confluence_html.append(
                    f'<ac:image><ri:attachment ri:filename="{image_name}" /></ac:image>'
                )
            self.tag_stack.append(('skip', None))

        elif tag in ['ul', 'ol']:
            self.confluence_html.append(f'<{tag}>')
            self.list_stack.append(tag)
            self.tag_stack.append((tag, None))

        elif tag == 'li':
            self.confluence_html.append('<li>')
            self.tag_stack.append((tag, None))

        elif tag == 'table':
            self.confluence_html.append('<table>')
            self.tag_stack.append((tag, None))

        elif tag == 'tr':
            self.confluence_html.append('<tr>')
            self.tag_stack.append((tag, None))

        elif tag in ['td', 'th']:
            colspan = attrs_dict.get('colspan', '')
            rowspan = attrs_dict.get('rowspan', '')
            attrs_str = ''
            if colspan:
                attrs_str += f' colspan="{colspan}"'
            if rowspan:
                attrs_str += f' rowspan="{rowspan}"'
            self.confluence_html.append(f'<{tag}{attrs_str}>')
            self.tag_stack.append((tag, None))

        elif tag == 'br':
            self.confluence_html.append('<br />')
            self.tag_stack.append(('skip', None))

        elif tag == 'code':
            self.confluence_html.append('<code>')
            self.tag_stack.append((tag, None))

        elif tag == 'pre':
            self.confluence_html.append('<ac:structured-macro ac:name="code"><ac:plain-text-body><![CDATA[')
            self.tag_stack.append(('pre', None))

        elif tag == 'blockquote':
            self.confluence_html.append('<blockquote>')
            self.tag_stack.append((tag, None))

        elif tag == 'hr':
            self.confluence_html.append('<hr />')
            self.tag_stack.append(('skip', None))

        elif tag in ['div', 'span']:
            # Generally skip divs and spans but process their content
            self.tag_stack.append(('passthrough', None))

        else:
            # Unknown tag - just pass through
            self.tag_stack.append(('passthrough', None))

    def handle_endtag(self, tag):
        if not self.tag_stack:
            return

        stack_tag, _ = self.tag_stack.pop()

        if stack_tag == 'skip' or stack_tag == 'a_skip':
            return

        if stack_tag == 'passthrough':
            return

        if stack_tag == 'pre':
            self.confluence_html.append(']]></ac:plain-text-body></ac:structured-macro>')
            return

        if tag == 'body':
            self.in_body = False
            return

        if self.in_body and stack_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'strong', 'em', 'u',
                                           'ul', 'ol', 'li', 'table', 'tr', 'td', 'th', 'code', 'blockquote']:
            self.confluence_html.append(f'</{stack_tag}>')
            if stack_tag in ['ul', 'ol'] and self.list_stack:
                self.list_stack.pop()

    def handle_data(self, data):
        if self.in_body and self.tag_stack:
            stack_tag, _ = self.tag_stack[-1] if self.tag_stack else ('', None)
            if stack_tag not in ['skip', 'a_skip']:
                # Clean up extra whitespace but preserve intentional spacing
                cleaned_data = data
                # Don't escape data - keep it as is for now, we'll handle it later if needed
                if cleaned_data.strip():
                    self.confluence_html.append(html.escape(cleaned_data))

    def get_confluence_html(self):
        """Returns the converted Confluence HTML"""
        return ''.join(self.confluence_html)


def convert_google_docs_to_confluence(html_file_path, output_file_path=None):
    """
    Convert a Google Docs HTML export to Confluence Storage Format

    Args:
        html_file_path: Path to the Google Docs HTML file
        output_file_path: Path to save the Confluence HTML (optional)

    Returns:
        str: The converted Confluence HTML
    """
    # Read the HTML file
    with open(html_file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Create converter and parse
    converter = GoogleDocsToConfluenceConverter()
    converter.feed(html_content)

    confluence_html = converter.get_confluence_html()

    # Clean up the HTML
    # Remove multiple consecutive empty paragraphs
    confluence_html = re.sub(r'(<p>\s*</p>\s*){2,}', '<p></p>', confluence_html)

    # Remove empty paragraphs at the start
    confluence_html = re.sub(r'^(<p>\s*</p>\s*)+', '', confluence_html)

    # Pretty print with indentation
    confluence_html = prettify_html(confluence_html)

    # Save to file if output path provided
    if output_file_path:
        with open(output_file_path, 'w', encoding='utf-8') as f:
            f.write(confluence_html)
        print(f"Converted HTML saved to: {output_file_path}")

    return confluence_html


def prettify_html(html_string):
    """Add basic indentation to HTML for readability"""
    lines = []
    indent_level = 0
    indent_str = '  '

    # Simple regex to find tags
    tag_pattern = re.compile(r'(<[^>]+>)')
    parts = tag_pattern.split(html_string)

    for part in parts:
        if not part:
            continue

        if part.startswith('</'):
            # Closing tag
            indent_level = max(0, indent_level - 1)
            lines.append(indent_str * indent_level + part)
        elif part.startswith('<') and not part.endswith('/>') and not part.startswith('<!'):
            # Opening tag
            lines.append(indent_str * indent_level + part)
            # Don't indent for self-closing-like tags or CDATA
            if 'CDATA' not in part and not any(part.startswith(f'<{t}') for t in ['br', 'hr', 'img', 'ac:image']):
                indent_level += 1
        elif part.startswith('<'):
            # Self-closing tag
            lines.append(indent_str * indent_level + part)
        else:
            # Text content
            text = part.strip()
            if text:
                lines.append(indent_str * indent_level + text)

    return '\n'.join(lines)


if __name__ == '__main__':
    # Default paths
    input_file = 'extracted_docs/JiraConfigurationBestPracticesGuidebook.md.html'
    output_file = 'confluence_output.html'

    # Allow command line arguments
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    print(f"Converting {input_file} to Confluence format...")
    print(f"Output will be saved to {output_file}")
    print()

    try:
        result = convert_google_docs_to_confluence(input_file, output_file)
        print(f"\nConversion complete!")
        print(f"Total length: {len(result)} characters")
        print(f"\nYou can now upload this HTML to Confluence.")
        print(f"Don't forget to also upload the images from the 'extracted_docs/images/' directory as attachments!")
    except Exception as e:
        print(f"Error during conversion: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
