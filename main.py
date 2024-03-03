from typing import Union
from pydantic import BaseModel

from fastapi import FastAPI, HTTPException
import requests
from gemini_api import text
import uvicorn


from chatgpt_api import chat_gpt_test,generate_response

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, port = 8000)
    
class PromptRequest(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#post endpoint for gemini api
@app.post("/ask-bard")
def gemini(prompt_request: PromptRequest):
    prompt = prompt_request.prompt
    response = text(prompt)
    print(f"This is the request prompt: {prompt}")
    # Assuming the `text` function properly handles the prompt
    # You would include your logic here to process the prompt and generate a response
    return {"response": response}


#post endpoint for perplexity api 
@app.post("/perplexity")
def post_perplexity_request():
    PERPLEXITY_API_KEY = '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'  # Replace with your API key
    url = "https://api.perplexity.ai/chat/completions"
    payload = {
    "model": "mistral-7b-instruct",
    "messages": [
        {
            "role": "system",
            "content": "Be precise and concise."
        },
        {
            "role": "user",
            "content": "How many stars are there in our galaxy?"
        }
      ]
    }
    headers = {
      "accept": "application/json",
      "content-type": "application/json",
      "Authorization": f"Bearer {PERPLEXITY_API_KEY}"
    }
    response = requests.post(url, json=payload, headers=headers) #api call
    #print(response.text)
    print("the backend response: {}".format(response)) #print the response from the backend to get an idea of the structure
    return {"message": response.json()}

#post endpoint for gpt-4 api:
@app.post("/gpt-4")
async def get_gpt4_response(prompt: str):
    response_message = await generate_response(prompt)
    return {"message": response_message}

@app.get("/gpt-4-test")
async def gpt_response():
    response = await chat_gpt_test()
    return {"Hello": response}