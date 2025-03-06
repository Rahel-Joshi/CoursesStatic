# semantic_search_static.py
import json
import numpy as np
from semantic_search import embed_text, extract_course_numbers  # Reuse helper functions

# Load the prebuilt knowledge base from the scraped HTML files
with open("cached_courses_from_scraped.json", "r", encoding="utf-8") as f:
    KNOWLEDGE_BASE = json.load(f)

def semantic_search(query, top_n=10):
    query_emb = embed_text(query)
    query_numbers = extract_course_numbers(query)
    scored_items = []
    for item in KNOWLEDGE_BASE:
        try:
            item_emb = np.array(item["embedding"])
        except Exception:
            continue
        similarity = np.dot(query_emb, item_emb)
        # Optionally boost similarity if some condition is met (e.g. matching keywords)
        scored_items.append((similarity, item))
    scored_items.sort(key=lambda x: x[0], reverse=True)
    top_records = [x[1] for x in scored_items[:min(top_n, len(scored_items))]]
    return top_records
