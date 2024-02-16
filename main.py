from typing import Union

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import httpx

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


#TODO: post endpoint for bard api 
BARD_API_ENDPOINT = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
API_KEY = "db8eea92532f3da2a5c66888c6761551de36487d"

# Define a request model for your endpoint
class QuestionRequest(BaseModel):
    question: str

@app.post("/ask-bard")
async def ask_bard(request: QuestionRequest):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                BARD_API_ENDPOINT,
                json={"contents": [{"parts": [{"text": request.question}]}]}, # Adjusted to match your API's expected payload structure
                headers={"Authorization": f"Bearer {API_KEY}"}
            )
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            raise HTTPException(status_code=e.response.status_code, detail=str(e))

        return response.json()

#post endpoint for perplexity api 
@app.post("/perplexity")
def post_perplexity_request():
    return {"message": "Perplexity created successfully"}

#post endpoint for gpt-4 api:
@app.post("/gpt-4")
def post_gpt4_request():
    return {"message": "GPT-4 created successfully"}




