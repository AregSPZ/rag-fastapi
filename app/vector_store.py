'''vector_store.py - vector database logic (indexing/storing and retrieval)'''

import re
import faiss
import numpy as np
from embeddings import get_embedding

dimension = 1536
index = faiss.IndexFlatL2(dimension)
documents = []

# Simplify the documents by keeping them lowercase and trimming punctuation'''
preprocess = lambda text: re.sub(r'[^a-z0-9\s]\?\.', '', text.lower())

def chunk_text(text: str, chunk_size: int = 200) -> list:
    # simple chunking by words
    words = text.split()
    return [
        ' '.join(words[i:i+chunk_size] for i in range(0, len(words), chunk_size))
    ]

def index_document(text: str):
    preprocessed = preprocess(text)
    chunks = chunk_text(preprocessed)
    for chunk in chunks:
        # pass/store as numpy arrays
        embedding = np.array([get_embedding(chunk)]).astype("float32")
        index.add(embedding)
        documents.append(chunk)

def query_index(query: str, top_k: int = 3):
    # convert to numpy array for similarity search between numpy arrays
    embedding = np.array([get_embedding(query)]).astype("float32")
    D, I  = index.search(embedding, top_k)
    # return the document text itself using the retrieved indices
    return [documents[i] for i in I[0] if i < len(documents)]