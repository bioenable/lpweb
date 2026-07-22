import os
import re
import glob

# Define the directory containing the HTML files (parent directory of scripts)
html_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Define the new LAUNCHPADi-Q link HTML snippet (inactive style)
launchpadiq_link_html = '''<a class="p-2 flex items-center text-sm text-gray-800 hover:text-blue-600 focus:outline-hidden focus:text-blue-600" href="LAUNCHPADi-Q-MCQ-quiz-web-application.htm">
               <svg class="shrink-0 size-4 me-3 md:me-2 block md:hidden" xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21.174 6.812a1 1 0 0 0-3.986-3.987L13.842 1a1 1 0 0 0-1.684.708L11.18 5.88a1 1 0 0 0 .708 1.684l3.128.971a1 1 0 0 0 1.684-.708l.971-3.128ZM11.879 11.88a1 1 0 0 0-1.684-.708L8.828 12.143a1 1 0 0 0-.708 1.684l.971 3.128a1 1 0 0 0 1.684.708l3.986-3.987ZM6.188 21.174a1 1 0 0 0 3.987-3.986L9.205 13.84a1 1 0 0 0-1.684-.708L3.354 16.3a1 1 0 0 0-.708 1.684l3.128.971a1 1 0 0 0 .708 1.684Z"/><circle cx="12" cy="12" r="10"/></svg>
              LAUNCHPADi-Q
            </a>'''

# Find the Home link pattern (could be active or inactive, href might vary)
# We will target the structure around the Home text more broadly
home_link_pattern = re.compile(
    r'(<a class="p-2 flex items-center text-sm )(?:text-blue-600|text-gray-800 hover:text-blue-600)(.*?>\s*<svg.*?</svg>\s*Home\s*</a>)', 
    re.DOTALL
)

# Corrected replacement involves making Home inactive and adding LAUNCHPADi-Q
def create_replacement(match):
    # Group 1 captures the start of the tag up to the class color
    # Group 2 captures the rest of the original Home anchor tag content
    original_anchor_tag_end = match.group(2)
    # Modify href if necessary, default to index.html
    updated_anchor_tag_end = re.sub(r'href="[^"]*"', 'href="index.html"', original_anchor_tag_end)
    
    home_link_inactive = f'<a class="p-2 flex items-center text-sm text-gray-800 hover:text-blue-600{updated_anchor_tag_end}'
    return f"{home_link_inactive}\n            {launchpadiq_link_html}"

# Iterate over .htm and .html files in the target directory
file_pattern = os.path.join(html_dir, '*.htm*')
html_files = glob.glob(file_pattern)

print(f"Found {len(html_files)} HTML files in {html_dir}")

updated_count = 0
skipped_count = 0

for filepath in html_files:
    filename = os.path.basename(filepath)
    print(f"Processing {filename}...")
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Check if the LAUNCHPADi-Q link already exists
        if 'href="LAUNCHPADi-Q-MCQ-quiz-web-application.htm"' in content:
             # Special handling for the target file itself to ensure Home is inactive
             if filename == "LAUNCHPADi-Q-MCQ-quiz-web-application.htm":
                 new_content, count = home_link_pattern.subn(create_replacement, content)
                 if count > 0:
                     with open(filepath, 'w', encoding='utf-8') as f:
                         f.write(new_content)
                     print(f" -> Updated Home link style in {filename}")
                     updated_count += 1
                 else:
                      print(f" -> Skipping {filename} (LAUNCHPADi-Q link present, Home style OK or pattern not found).")
                      skipped_count +=1
             else:
                print(f" -> Skipping {filename} (LAUNCHPADi-Q link already present).")
                skipped_count +=1
                continue # Skip if link exists and it's not the target file
        
        # If the link doesn't exist, find the home link and insert the new one after it
        new_content, count = home_link_pattern.subn(create_replacement, content)

        if count > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f" -> Successfully added LAUNCHPADi-Q link to {filename}")
            updated_count += 1
        else:
            print(f" -> Failed to find Home link pattern in {filename}. Skipping.")
            skipped_count += 1

    except Exception as e:
        print(f" -> Error processing {filename}: {e}")
        skipped_count += 1


print(f"\\nFinished processing.")
print(f"Updated files: {updated_count}")
print(f"Skipped files: {skipped_count}") 