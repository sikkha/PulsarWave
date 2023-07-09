import json
import openai
import os


def process_text(user_input, context, maxtoken=100, project="flaskgeopolitics", location="us-central1"):
    # initialize

    # Start a chat sequence
    messages = [
        {"role": "system", "content": "You are a geopolitical expert."},
        {"role": "system", "content": context},
        {"role": "user", "content": user_input}
    ]

    # Make a completion call
    oyyo = openai.ChatCompletion.create(
        model="gpt-3.5k-turbo-16k",
        messages=messages
    )

    # Print the assistant's response
    response = oyyo['choices'][0]['message']['content']


    # return response
    return response


def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def read_json(file_path):
    with open(file_path, "r") as file:
        return json.load(file)

data = read_json("/tmp/keepweb.txt")

for item in data:
    subject = item['subject']
    url = item['url']
    extracted_data = item['extracted_data']
    context_caption = """Please make headline caption not more than 3 words."""
    context_summarize = """Please make summarization over the input text."""

    if "JavaScript is disabled in this browser." in extracted_data:
        # In this case, the page could not be scraped.
        caption = process_text(subject, context_caption)
        short_description = process_text(subject, context_summarize)
        print(f"{item['story_number']}: {caption}: {short_description}: {url}")
    else:
        # In this case, the page was successfully scraped.
        caption = process_text(subject, context_caption)
        long_description = process_text(extracted_data, context_summarize)
        print(f"{item['story_number']}: {caption}: {long_description}: {url}")



