from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter(prefix="/api/v1")

@router.post("/chat/completions")
async def chat_completion(prompt: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/v1/chat/completions",
                json={
                    "model": "qwen2.5:0.5b",
                    "messages": [{"role": "user", "content": prompt}]
                }
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))

@router.post("/embeddings")
async def get_embeddings(text: str):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(
                "http://localhost:11434/v1/embeddings",
                json={
                    "model": "nomic-embed-text:latest",
                    "input": text
                }
            )
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        raise HTTPException(status_code=e.response.status_code, detail=str(e))
