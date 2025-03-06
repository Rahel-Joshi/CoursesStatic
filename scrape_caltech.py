import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Base URL for the undergraduate students section
BASE_URL = "https://catalog.caltech.edu/current/"

# Directory where scraped pages will be saved
OUTPUT_DIR = "scraped_pages"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

# Set to track visited URLs
visited = set()

def safe_filename(url):
    """Generate a safe filename from a URL by removing protocol and replacing non-alphanumeric characters."""
    parsed = urlparse(url)
    path = parsed.netloc + parsed.path
    safe = re.sub(r'[^a-zA-Z0-9]', '_', path)
    return safe + ".html"

def scrape_page(url):
    """Fetch the page content from the given URL."""
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to fetch {url}: {response.status_code}")
            return None
        return response.text
    except Exception as e:
        print(f"Error fetching {url}: {str(e)}")
        return None

def extract_links(html, base):
    """Extract all unique links from the HTML that start with the base URL."""
    soup = BeautifulSoup(html, "html.parser")
    links = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        full_url = urljoin(BASE_URL, href)
        if full_url.startswith(base):
            links.add(full_url)
    return links

def crawl(url, base):
    """Recursively crawl URLs starting from the given URL, saving each page to disk."""
    if url in visited:
        return
    print(f"Crawling: {url}")
    visited.add(url)
    html = scrape_page(url)
    if html is None:
        return

    # Save the page HTML to a file
    filename = os.path.join(OUTPUT_DIR, safe_filename(url))
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Saved: {filename}")

    # Extract links on this page and crawl them recursively
    links = extract_links(html, base)
    for link in links:
        crawl(link, base)

if __name__ == "__main__":
    crawl(BASE_URL, BASE_URL)
