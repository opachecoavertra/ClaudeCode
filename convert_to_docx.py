#!/usr/bin/env python3
"""
Convert Confluence HTML to Word Document (DOCX)

This script converts the Confluence HTML output to a Word document
that can be imported directly into Confluence.
"""

from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from html.parser import HTMLParser
import re
import sys


class HTMLToDocxConverter(HTMLParser):
    """Converts HTML to DOCX format"""

    def __init__(self, document):
        super().__init__()
        self.doc = document
        self.current_paragraph = None
        self.current_run = None
        self.tag_stack = []
        self.list_stack = []
        self.in_table = False
        self.current_table = None
        self.current_row = None
        self.current_cell = None
        self.list_items = []
        self.current_list_type = None
        self.bold = False
        self.italic = False
        self.underline = False

    def handle_starttag(self, tag, attrs):
        attrs_dict = dict(attrs)

        # Skip Confluence-specific tags
        if tag in ['ac:image', 'ri:attachment', 'ac:link', 'ri:url', 'ac:structured-macro', 'ac:plain-text-body']:
            self.tag_stack.append(('skip', None))
            return

        if tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']:
            level = int(tag[1])
            self.current_paragraph = self.doc.add_heading(level=level)
            self.current_run = None
            self.tag_stack.append((tag, self.current_paragraph))

        elif tag == 'p':
            self.current_paragraph = self.doc.add_paragraph()
            self.current_run = None
            self.tag_stack.append((tag, self.current_paragraph))

        elif tag in ['strong', 'b']:
            self.bold = True
            self.tag_stack.append(('bold', None))

        elif tag in ['em', 'i']:
            self.italic = True
            self.tag_stack.append(('italic', None))

        elif tag == 'u':
            self.underline = True
            self.tag_stack.append(('underline', None))

        elif tag == 'br':
            if self.current_paragraph:
                self.current_paragraph.add_run('\n')
            self.tag_stack.append(('skip', None))

        elif tag in ['ul', 'ol']:
            self.current_list_type = tag
            self.list_stack.append(tag)
            self.tag_stack.append((tag, None))

        elif tag == 'li':
            # Will be handled in handle_data
            self.tag_stack.append(('li', None))

        elif tag == 'table':
            # Count rows and columns first (simplified - we'll handle it dynamically)
            self.in_table = True
            self.current_table = None  # Will create when we know size
            self.tag_stack.append(('table', None))

        elif tag == 'tr':
            self.tag_stack.append(('tr', None))

        elif tag in ['td', 'th']:
            self.tag_stack.append((tag, None))

        else:
            self.tag_stack.append(('skip', None))

    def handle_endtag(self, tag):
        if not self.tag_stack:
            return

        stack_tag, _ = self.tag_stack.pop()

        if stack_tag == 'skip':
            return

        if stack_tag in ['bold', 'b', 'strong']:
            self.bold = False
        elif stack_tag in ['italic', 'i', 'em']:
            self.italic = False
        elif stack_tag == 'underline':
            self.underline = False
        elif stack_tag in ['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p']:
            self.current_paragraph = None
            self.current_run = None
        elif stack_tag in ['ul', 'ol']:
            if self.list_stack:
                self.list_stack.pop()
            self.current_list_type = self.list_stack[-1] if self.list_stack else None

    def handle_data(self, data):
        cleaned_data = data.strip()
        if not cleaned_data:
            return

        if self.tag_stack and self.tag_stack[-1][0] == 'skip':
            return

        # Check if we're in a list item
        in_list_item = any(tag == 'li' for tag, _ in self.tag_stack)

        if in_list_item:
            # Create a list paragraph
            list_type = self.current_list_type or 'ul'
            if list_type == 'ul':
                p = self.doc.add_paragraph(cleaned_data, style='List Bullet')
            else:
                p = self.doc.add_paragraph(cleaned_data, style='List Number')

            # Apply formatting if needed
            if self.bold or self.italic or self.underline:
                for run in p.runs:
                    if self.bold:
                        run.bold = True
                    if self.italic:
                        run.italic = True
                    if self.underline:
                        run.underline = True
        else:
            # Regular text in paragraph
            if self.current_paragraph is None:
                self.current_paragraph = self.doc.add_paragraph()

            run = self.current_paragraph.add_run(cleaned_data)

            if self.bold:
                run.bold = True
            if self.italic:
                run.italic = True
            if self.underline:
                run.underline = True

            self.current_run = run


def convert_html_to_docx(html_file, output_file):
    """
    Convert HTML file to DOCX

    Args:
        html_file: Path to HTML file
        output_file: Path to output DOCX file
    """
    # Read HTML
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Remove Confluence-specific XML tags for cleaner conversion
    html_content = re.sub(r'<ac:image>.*?</ac:image>', '[Image]', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<ac:link>.*?</ac:link>', '', html_content, flags=re.DOTALL)
    html_content = re.sub(r'<ac:structured-macro.*?</ac:structured-macro>', '', html_content, flags=re.DOTALL)

    # Create document
    doc = Document()

    # Set document properties
    doc.core_properties.title = "Jira Configuration Best Practices Guidebook"
    doc.core_properties.author = "Converted from Google Docs"

    # Parse and convert
    converter = HTMLToDocxConverter(doc)
    converter.feed(html_content)

    # Save
    doc.save(output_file)
    print(f"✓ Word document created: {output_file}")
    return output_file


if __name__ == '__main__':
    input_file = 'confluence_output.html'
    output_file = 'Jira_Configuration_Best_Practices.docx'

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
    if len(sys.argv) > 2:
        output_file = sys.argv[2]

    print(f"Converting {input_file} to Word document...")
    convert_html_to_docx(input_file, output_file)
    print(f"\n✓ Conversion complete!")
    print(f"\nNext steps:")
    print(f"1. Download the file: {output_file}")
    print(f"2. Go to Confluence: https://avertra.atlassian.net/wiki/spaces/PD/pages/2861006849")
    print(f"3. Click 'Edit' → '...' menu → 'Import Word Document'")
    print(f"4. Upload {output_file}")
    print(f"5. Review and publish!")
    print(f"\nNote: You'll still need to upload the images manually from extracted_docs/images/")
