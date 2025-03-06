# semantic_search.py
import re
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the embedding model (this may download model weights on first run)
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_text(text: str) -> np.ndarray:
    """Encodes text into an embedding using Sentence Transformers."""
    return embedding_model.encode(text)

def extract_course_numbers(text: str):
    """
    Extracts course numbers from a text string.
    For example, from "cs 38" it returns ['38'].
    """
    return re.findall(r'cs\s*([0-9]+)', text, flags=re.IGNORECASE)
