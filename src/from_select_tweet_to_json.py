import os
import json

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

data = []

with open("/tmp/select_tweet.txt", "r") as file:
    lines = file.readlines()

for i, line in enumerate(lines):
    subject = line.split("https://")[0].strip().replace("'", "")
    url = "https://" + line.split("https://")[1].strip().replace("'", "").replace("\"", "")
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
    os.remove('/tmp/tmp_keepweb.txt')

with open("/tmp/keepweb.txt", "w") as file:
    json.dump(data, file, indent=4)


