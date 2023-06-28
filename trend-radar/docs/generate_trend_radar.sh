#!/bin/bash

# Step 1: Backup the original index.html
cp index.html "index.html,$(date +%Y-%m-%d_%H-%M-%S)_back"

# Step 2: Generate the header
python3 print_header.py

# Step 3: Loop through the entries in entry.txt and call print_entry.py
while IFS=',' read -r quadrant ring label link active moved
do
    python3 print_entry.py "$quadrant" "$ring" "$label" "$link" "$active" "$moved"
done < entry.txt

# Step 4: Generate the footer
python3 print_footer.py

# Step 5: rewrite the index.html
cp new_index.html index.html

