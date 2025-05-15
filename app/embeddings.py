'''embeddings.py - generate embeddings for vector storing'''

from google import genai

client = genai.Client(api_key=api_key)

def get_embedding(text):

    result = client.models.embed_content(
        model="gemini-embedding-exp-03-07",
        contents=text,
        # optimize the embeddings for semantic search
        config=genai.types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
    )
    
    embeddings = list(result.embeddings[0])[0][-1]
    print(embeddings)

    return embeddings
