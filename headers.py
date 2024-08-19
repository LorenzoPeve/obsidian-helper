import re
from pathlib import Path

def extract_headings(markdown_file):
    # Extract the filename without extension
    filename = Path(markdown_file).stem

    # Read the content of the markdown file
    with open(markdown_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Use regex to find all headings (lines starting with #)
    headings = re.findall(r'^(#+)\s+(.+)', content, re.MULTILINE)

    # Generate the list of bullets
    bullet_list = [
        f'[[{filename}#{heading}|{heading}]]' 
        for _, heading in headings
    ]

    return bullet_list

# Example usage
markdown_file = r"C:\Users\lpeve\iCloudDrive\iCloud~md~obsidian\LorenzoTreasury\3.12.0 Data Engineering and Cloud\Azure\Azure AI Search Indexer Running and Scheduling.md"
bullets = extract_headings(markdown_file)
for bullet in bullets:
    print(bullet)
