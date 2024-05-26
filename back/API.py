from fastapi import FastAPI
import random

app = FastAPI()

# try this:
# python -m uvicorn API:app --reload
# cd C:\Users\jaede\OneDrive\Documents\!!! school things\11th\res\XHub-arXiv-Warriors-Hub-\back

@app.get("/AI")
async def read_root():
    rn = random.randint(0,100) 
    return {"Message": "Congrats! This is your first API!", "data": 10, "random_number" : rn}