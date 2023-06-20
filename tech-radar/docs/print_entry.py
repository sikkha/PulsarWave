import re
import argparse

def generate_entry(quadrant, ring, label, link, active, moved):
    entry = f'{{"quadrant": {quadrant}, "ring": {ring}, "label": "{label}", "link": "{link}", "active": {str(active).lower()}, "moved": {moved}}}'
    return entry

def update_index_html(file_path, new_entry):
    with open(file_path, 'a', encoding='utf-8') as file:
        entry_str = f'      {new_entry},\n'
        file.write(entry_str)

def main(args):
    file_path = 'new_index.html'
    new_entry = generate_entry(args.quadrant, args.ring, args.label, args.link, args.active, args.moved)
    update_index_html(file_path, new_entry)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a new entry to the Tech Radar")
    parser.add_argument("quadrant", type=int, help="Quadrant number")
    parser.add_argument("ring", type=int, help="Ring number")
    parser.add_argument("label", type=str, help="Label for the technology")
    parser.add_argument("link", type=str, help="Link for the technology")
    parser.add_argument("active", type=bool, help="Active status (True or False)")
    parser.add_argument("moved", type=int, help="Moved status (integer)")

    args = parser.parse_args()
    main(args)

