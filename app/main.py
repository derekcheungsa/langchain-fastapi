from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain.retrievers import WikipediaRetriever

app = FastAPI()

class Query(BaseModel):
    query: str

app = FastAPI()

@app.post("/query/")
async def process_query(query: Query):
    retriever = WikipediaRetriever()
    docs = retriever.get_relevant_documents(query=query.query)
    response = docs[0].page_content[:400]
    return {"reply": response }