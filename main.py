from fastapi import FastAPI
 
app = FastAPI(title = "Excuse Generator")

@app.get("/")
def root():
    return{"name": "Excuse Generator", "try": "/excuse?situation=I forgot my homework"}

@app.get("/excuse")
async def get_excuse(situation: str):
    return {"situation": situation, "excuse": "coming soon!"}