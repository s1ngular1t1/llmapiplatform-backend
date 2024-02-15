from typing import Union

from fastapi import FastAPI

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
    return {"message": "Perplexity created successfully"}

#post endpoint for gpt-4 api:
@app.post("/gpt-4")
def post_gpt4_request():
    return {"message": "GPT-4 created successfully"}




