'''main.py - App Orchestration'''

import uvicorn
from fastapi import FastAPI, UploadFile, File
from fastapi.concurrency import run_in_threadpool
from vector_store import index_document
from schemas import QueryRequest
from response_generation import get_response

app = FastAPI()

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    '''Add a new file into the vector store'''
    # read the uploaded file on the side (no blocking)
    text = await file.read()
    # decode the file text into a string (happens only after the full text is read, so we wait the previous line)
    content = text.decode("utf-8")
    # index (add) the new content into the existing vector database
    index_document(content)
    return {"message": "Document indexed successfully."}

# posting the query and getting back the response, that's why POST 
# the prompt is too large to fit into URL so GET won't work out
@app.post("/query")
async def query_docs(query: QueryRequest):

    response = get_response(query.query)
    return {'results': response}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)