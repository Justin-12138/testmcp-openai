from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import httpx

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


API_KEY = "your-secret-api-key"  # 实际使用中应使用环境变量

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int = 100

class EmbeddingRequest(BaseModel):
    text: str

async def verify_api_key(api_key: str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key

@app.post("/chat/completions")
async def chat_completion(request: ChatRequest, api_key: str = Depends(verify_api_key)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/v1/chat/completions",
            json={
                "model": "qwen2.5:0.5b",
                "messages": [{"role": "user", "content": request.prompt}],
                "max_tokens": request.max_tokens
            }
        )
        return response.json()

@app.post("/embeddings")
async def embeddings(request: EmbeddingRequest, api_key: str = Depends(verify_api_key)):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            "http://localhost:11434/v1/embeddings",
            json={
                "model": "nomic-embed-text:latest",
                "input": request.text
            }
        )
        return response.json()

@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
