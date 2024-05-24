from fastapi import FastAPI

app = FastAPI()
"""
try this:
python -m uvicorn API:app --reload
cd C:\Users\jaede\OneDrive\Documents\!!! school things\11th\res\XHub-arXiv-Warriors-Hub-\back
"""
@app.get("/example")
async def read_root():
    return {"Message": "Congrats! This is your first API!", "data": 0}