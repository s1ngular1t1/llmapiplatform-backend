from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

#TODO: post endpoint for bard api 
@app.post("/bard")
def post_bard_request():
    return {"message": "Bard created successfully"}

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
def post_gpt4_request():
    return {"message": "GPT-4 created successfully"}




