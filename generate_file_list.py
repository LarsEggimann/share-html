#!/usr/bin/env python3
import os
import re

def main():
    # Find all HTML files except index.html
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html') and file != 'index.html':
                filepath = os.path.relpath(os.path.join(root, file), '.')
                html_files.append(filepath)
    
    print(f"Found HTML files: {html_files}")
    
    # Read index.html
    with open('index.html', 'r') as f:
        content = f.read()
    
    # Create the JavaScript array string
    files_array = '[' + ',\n    '.join([f'"{file}"' for file in html_files]) + ']'
    
    # Replace the placeholder in the script tag
    content = re.sub(
        r'// File list will be injected here by GitHub Actions',
        f'// File list injected by GitHub Actions\n    window.htmlFiles = {files_array};',
        content
    )
    
    # Write back to index.html
    with open('index.html', 'w') as f:
        f.write(content)
    
    print("Updated index.html successfully!")
    print(f"Injected {len(html_files)} HTML files into the page")

if __name__ == '__main__':
    main()
