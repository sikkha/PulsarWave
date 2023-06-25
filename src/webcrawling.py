from urllib.parse import urlparse
from bs4 import BeautifulSoup
import os
import requests
import argparse

def crawl(url):
    # Parse the URL and get the domain
    local_domain = urlparse(url).netloc

    if "t.co" in local_domain:
        # Follow the redirection if it's a Twitter short URL
        try:
            response = requests.get(url)
            url = response.url
            local_domain = urlparse(url).netloc
        except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as err:
            print(f"An error occurred while fetching {url}: {err}")
            return

    if "https://twitter.com/i/web/status" in url:
        print(f"Skipping {url}: URL pattern not supported.")
        return None

    print(f'Crawling URL: {url}')  # For debugging and to see the progress

    # Get the text from the URL using BeautifulSoup
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises a HTTPError if the status is 4xx, 5xx
    except (requests.exceptions.RequestException, requests.exceptions.HTTPError) as err:
        print(f"An error occurred while fetching {url}: {err}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")

    # Get the text but remove the tags
    text = soup.get_text()

    # If the crawler gets to a page that requires JavaScript, it will stop the crawl
    if "You need to enable JavaScript to run this app." in text:
        print(f"Unable to parse page {url} due to JavaScript being required")
        return None
    else:
        return text  # Return the text of the page
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Crawl a URL and print its content')
    parser.add_argument('url', type=str, help='The URL to crawl')

    args = parser.parse_args()

    # Run the function
    text = crawl(args.url)
    if text:
        print(text)
