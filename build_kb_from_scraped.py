import os
import json
from bs4 import BeautifulSoup
from semantic_search import embed_text

# Directory where your scraped HTML pages are stored
SCRAPED_DIR = "scraped_pages"
OUTPUT_FILE = "cached_courses_from_scraped.json"

all_records = []

def safe_file_id(filename):
    """Generate a record id from the filename (removing the .html extension)."""
    return filename.replace(".html", "")

# Iterate over all HTML files in the scraped_pages directory
for fname in os.listdir(SCRAPED_DIR):
    if fname.endswith(".html"):
        filepath = os.path.join(SCRAPED_DIR, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()
        soup = BeautifulSoup(html, "html.parser")
        
        # Extract the text content: you might extract <body> text or customize this further
        body = soup.find("body")
        if body:
            text = body.get_text(separator=" ", strip=True)
        else:
            text = soup.get_text(separator=" ", strip=True)
        
        record = {
            "id": safe_file_id(fname),
            "text": text,
            "metadata": {
                "filename": fname,
                # Optionally, you could add more metadata here if available.
            },
            "embedding": embed_text(text).tolist()
        }
        all_records.append(record)
        print(f"Processed {fname}")

# Save all records to a JSON file
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(all_records, f, indent=4)

print(f"Created knowledge base with {len(all_records)} records in {OUTPUT_FILE}")
