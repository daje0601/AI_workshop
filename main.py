
import os
import time
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse, Response

from llm_service import chat_openai, chat_runpod


app = FastAPI()


@app.get("/health")
async def health_check():
    return {"message": "I am healthy"}



class ChatRequest(BaseModel):
    query: str              # 필수 필드
    provider: str = "openai"  # "openai" or "runpod"
    model: str = "gpt-4o-mini"  # 모델 이름 (OpenAI용)
    streaming: bool = False    # 스트리밍 여부

@app.post("/chat")
async def chat(request: ChatRequest):

    start_time = time.time()

    if request.provider == "openai":
        result = await chat_openai(request.model, request.query, request.streaming)
        if request.streaming:
            response = StreamingResponse(result, media_type="text/plain")
        else:
            response = Response(result, media_type="text/plain")
    
    elif request.provider == "runpod":
        # RunPod는 스트리밍 미지원
        content = await chat_runpod(request.query)
        response = Response(content, media_type="text/plain")
    
    else:
        response = Response(f"Unknown provider: {request.provider}", status_code=400)

    end_time = time.time()
    duration = end_time - start_time
    print(f"Response time: {duration:.2f} seconds")

    return response