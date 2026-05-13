from fastapi import FastAPI
from dotenv import load_dotenv
import httpx
import os
 
load_dotenv()
KEY = os.getenv("HACKCLUB_AI_KEY")

app = FastAPI(title = "Excuse Generator")

@app.get("/")
def root():
    return{"name": "Excuse Generator", "try": "/excuse?situation=I forgot my homework"}

@app.get("/excuse")
async def get_excuse(situation: str):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "https://ai.hackclub.com/chat/completions",
            headers={"Authorization": f"Bearer {KEY}"},
            json={
                "messages": [
                    {"role": "system", "content": "You generate funny, creative, slightly unhinged excuses. One sentence only. No quotes around your answer."},
                    {"role": "user", "content":  f"Give me an excuse for: {situation}"} ,
                        ],   
                    }
            
        )
data = response.json()
excuese = data["choices"][0]["message"]["content"]]