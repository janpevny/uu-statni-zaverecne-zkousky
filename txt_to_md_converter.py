import os
import re
from pathlib import Path
from html import unescape
from bs4 import BeautifulSoup
import markdownify

def html_to_markdown(html_content):
    """Convert HTML content to Markdown"""
    # Clean up the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Convert to markdown using markdownify
    markdown_content = markdownify.markdownify(str(soup), heading_style="ATX")
    
    # Clean up extra whitespace
    markdown_content = re.sub(r'\n\s*\n\s*\n', '\n\n', markdown_content)
    markdown_content = markdown_content.strip()
    
    return markdown_content

def convert_txt_to_md(input_file, output_file):
    """Convert a single TXT file to Markdown format"""
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    
    lines = content.split('\n')
    markdown_lines = []
    first_h1_added = False
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        # Split line by tab to separate the title and HTML content
        parts = line.split('\t', 1)
        if len(parts) != 2:
            continue
            
        title_part = parts[0].strip()
        html_part = parts[1].strip()
        
        # Remove quotes from HTML part
        if html_part.startswith('"') and html_part.endswith('"'):
            html_part = html_part[1:-1]
        
        # Parse title - extract number and topic
        title_match = re.match(r'^(\d+)\.\s*(.+?)\s*-\s*(.+)$', title_part)
        if not title_match:
            continue
            
        number = title_match.group(1)
        main_topic = title_match.group(2).strip()
        sub_topic = title_match.group(3).strip()
        
        # Create markdown headers - only first one gets H1, rest are H2
        if not first_h1_added:
            markdown_lines.append(f"# {number}. {main_topic}")
            markdown_lines.append("")
            first_h1_added = True
        
        markdown_lines.append(f"## {sub_topic}")
        markdown_lines.append("")
        
        # Convert HTML to markdown
        markdown_content = html_to_markdown(html_part)
        markdown_lines.append(markdown_content)
        markdown_lines.append("")
    
    # Write to output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(markdown_lines))

def process_all_txt_files():
    """Process all TXT files in the anki directory"""
    input_dir = Path("Softwarový vývoj/anki/Backendové systémy")
    output_dir = Path("Softwarový vývoj/Backendové systémy")
    
    if not input_dir.exists():
        print(f"Input directory {input_dir} does not exist!")
        return
    
    txt_files = list(input_dir.glob("*.txt"))
    if not txt_files:
        print(f"No TXT files found in {input_dir}")
        return
    
    print(f"Found {len(txt_files)} TXT files to convert:")
    
    for txt_file in txt_files:
        # Create corresponding .md filename
        md_filename = txt_file.stem + ".md"
        output_file = output_dir / md_filename
        
        print(f"Converting {txt_file.name} -> {output_file}")
        
        try:
            convert_txt_to_md(txt_file, output_file)
            print(f"[OK] Successfully converted {txt_file.name}")
        except Exception as e:
            print(f"[ERROR] Error converting {txt_file.name}: {e}")

if __name__ == "__main__":
    print("TXT to Markdown Converter")
    print("=" * 40)
    process_all_txt_files()
    print("Conversion complete!")