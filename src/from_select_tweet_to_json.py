import os
import json

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

data = []

with open("/tmp/select_tweet.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    #for debug
    #print(f'Line: {line}')  # Print the line before splitting
    #split_line = line.split("https://")
    #print(f'Split line: {split_line}')  # Print the split line

    if line.strip() == '':
        continue  # Skip this line if it's empty or just contains a newline

    split_line = line.split("https://")
    if len(split_line) < 2:
        print(f'Invalid line: "{line}"')
        continue  # Skip this line and move to the next



    subject = line.split("https://")[0].strip().replace("'", "")
    url = "https://" + line.split("https://")[1].strip().replace("'", "").replace("\"", "")

    #for debug
    #print(url)

    command = f'python3 webcrawling.py {url} > /tmp/tmp_keepweb.txt'
    os.system(command)
    content_fromweb = read_file('/tmp/tmp_keepweb.txt')
    story = {
        "story_number": i+1,
        "subject": subject,
        "url": url,
        "extracted_data": content_fromweb
    }
    data.append(story)

    # Remove the temporary file after use
    #os.remove('/tmp/tmp_keepweb.txt')

with open("/tmp/keepweb.txt", "w") as file:
    json.dump(data, file, indent=4)

