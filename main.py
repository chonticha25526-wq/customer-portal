from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Document(BaseModel):
    doc_id: str
    title: str
    sender: str
    current_status: str
    next_approver: str

db_documents = {}

@app.post("/documents/submit")
def submit_document(doc: Document):
    if doc.doc_id in db_documents:
        raise HTTPException(status_code=400, detail="Document ID already exists")
    db_documents[doc.doc_id] = doc
    return {"message": "Document submitted successfully", "document": doc}

@app.get("/")
def home():
    return {"message": "Document Routing API is running!"}
