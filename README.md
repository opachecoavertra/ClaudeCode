# Google Docs to Confluence HTML Converter

This project converts Google Docs documents (exported as HTML) to Confluence Storage Format, making it easy to migrate documentation from Google Docs to Confluence.

## Features

- ✅ Converts Google Docs HTML to Confluence Storage Format (XHTML)
- ✅ Preserves document structure (headings, lists, tables, paragraphs)
- ✅ Handles text formatting (bold, italic, underline)
- ✅ Converts images to Confluence attachment references
- ✅ Supports nested lists, tables, and code blocks
- ✅ Clean, readable output with proper indentation

## Quick Start

### 1. Export Your Google Doc

1. Open your Google Doc
2. Go to **File → Download → Web Page (.html, zipped)**
3. Extract the ZIP file - you'll get an HTML file and an `images` folder

### 2. Convert to Confluence Format

```bash
python3 convert_to_confluence.py input.html output.html
```

Or use the defaults:
```bash
python3 convert_to_confluence.py
```

This will convert `extracted_docs/JiraConfigurationBestPracticesGuidebook.md.html` to `confluence_output.html`

### 3. Upload to Confluence

#### Option A: Using Confluence REST API

```python
# See confluence_uploader.py for a complete example
import requests

confluence_url = "https://your-domain.atlassian.net"
page_id = "your-page-id"
auth = ("your-email@example.com", "your-api-token")

# Read the converted HTML
with open('confluence_output.html', 'r') as f:
    html_content = f.read()

# Update the page
url = f"{confluence_url}/rest/api/content/{page_id}"
data = {
    "version": {"number": current_version + 1},
    "title": "Your Page Title",
    "type": "page",
    "body": {
        "storage": {
            "value": html_content,
            "representation": "storage"
        }
    }
}

response = requests.put(url, json=data, auth=auth)
```

#### Option B: Manual Upload

1. Create or edit a page in Confluence
2. Switch to the **Storage Format** editor (you may need to install a plugin or use the REST API)
3. Paste the converted HTML
4. Upload images from the `extracted_docs/images/` folder as attachments to the page

## Project Structure

```
.
├── convert_to_confluence.py          # Main converter script
├── extracted_docs/                    # Extracted Google Docs export
│   ├── JiraConfigurationBestPracticesGuidebook.md.html
│   └── images/                        # Images from the document (21 images)
│       ├── image1.png
│       ├── image2.png
│       └── ...
├── confluence_output.html             # Converted Confluence HTML
└── README.md                          # This file
```

## Example Output

The converter transforms Google Docs HTML like this:

**Input (Google Docs HTML):**
```html
<html><head><style>...</style></head><body>
<h1 class="c15" id="h.123"><span class="c4">Create a Project</span></h1>
<p class="c2"><span class="c0">Think of a Jira project...</span></p>
</body></html>
```

**Output (Confluence Storage Format):**
```html
<h1>Create a Project</h1>
<p>Think of a Jira project as your team's home base for getting work done.</p>
```

## Converted Document Stats

- **Original file size:** 225 KB (Google Docs HTML with inline CSS)
- **Converted size:** 56 KB (clean Confluence HTML)
- **Images:** 21 images referenced as attachments
- **Structure:** 11 main sections (H1), 30 subsections (H2), 5 H3s, 5 H4s

## Requirements

- Python 3.6+
- No external dependencies (uses only Python standard library)

## How It Works

1. **Parse HTML:** Uses Python's `HTMLParser` to parse the Google Docs HTML
2. **Convert Tags:** Maps Google Docs HTML tags to Confluence Storage Format
   - Regular HTML tags (h1-h6, p, ul, ol, li, table, etc.) are preserved
   - Google Docs-specific classes and styles are stripped
   - Images are converted to Confluence attachment references
   - Code blocks are wrapped in Confluence macros
3. **Clean Output:** Removes empty paragraphs and adds indentation for readability
4. **Save:** Outputs clean, valid Confluence Storage Format HTML

## Confluence Storage Format

Confluence uses a specific XHTML format called "Storage Format". Key elements:

- **Images:** `<ac:image><ri:attachment ri:filename="image.png" /></ac:image>`
- **Links:** `<ac:link><ri:url ri:value="http://example.com" /></ac:link>`
- **Code blocks:** `<ac:structured-macro ac:name="code">...</ac:structured-macro>`
- **Standard HTML:** h1-h6, p, ul, ol, li, table, tr, td, th, strong, em, u

## Customization

To customize the conversion, edit `convert_to_confluence.py`:

- **Add custom tag handling:** Modify the `handle_starttag()` method
- **Change formatting:** Update the tag mappings in the converter class
- **Add macros:** Insert Confluence macros for special content types

## Next Steps

To build a fully automated solution:

1. **Google Docs API integration:** Fetch documents programmatically
2. **Confluence REST API integration:** Automatically create/update pages
3. **Image upload:** Automatically upload images as attachments
4. **Batch processing:** Convert multiple documents at once
5. **CI/CD integration:** Auto-sync docs from Google Docs to Confluence

## License

MIT License - feel free to use and modify as needed.

## Contributing

Contributions welcome! Please open an issue or PR on GitHub.
