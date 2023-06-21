import re

def generate_entry(quadrant, ring, label, link, active, moved):
    entry = {
        "quadrant": quadrant,
        "ring": ring,
        "label": label,
        "link": link,
        "active": active,
        "moved": moved
    }
    return entry

def update_index_html(file_path, new_entry):
    with open(file_path, 'r', encoding='utf-8') as file:
        contents = file.read()

    pattern = r'(\s*//ENTRIES\s*\n\s*entries: \[\s*\n)(.*)(\s*\n\s*//ENTRIES)'
    match = re.search(pattern, contents, re.DOTALL)

    if not match:
        raise ValueError("Could not find the entries section in index.html")

    before_entries = match.group(1)
    entries_text = match.group(2)
    after_entries = match.group(3)

    entry_str = f'      {new_entry},\n'
    updated_entries = entries_text + entry_str

    updated_contents = before_entries + updated_entries + after_entries

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(updated_contents)

# Example usage:
file_path = 'index.html'

quadrant = 1
ring = 1
label = "Docker"
link = "https://www.docker.com/"
active = True
moved = 0

new_entry = generate_entry(quadrant, ring, label, link, active, moved)
update_index_html(file_path, new_entry)

