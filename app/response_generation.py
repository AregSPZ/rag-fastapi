from google import genai
from vector_store import query_index

client = genai.Client(api_key=api_key)

def get_response(user_prompt):

    retrieved_chunks = query_index(user_prompt)

    prompt = f"""Given the following research paper excerpts, answer the user's query: {user_prompt}.
                
                Context:

                {retrieved_chunks}"""
    

    response = client.models.generate_content(
        model="gemini-2.5-pro-preview-05-06",
        contents=prompt
    )

    return response.text
