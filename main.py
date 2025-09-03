
import os
import time
from fastapi import FastAPI
from pydantic import BaseModel, Field
from fastapi.responses import StreamingResponse, Response

from lifespan import stream_from_openai, chat_from_openai


app = FastAPI()


@app.get("/health")
async def health_check():
    return {"message": "I am healthy"}



class ChatRequest(BaseModel):
    query: str              # 필수 필드
    llm: str = "gpt-4o-mini"  # 선택 필드 (기본값 있음)
    streaming: bool = False    # 선택 필드 (기본값 있음)

@app.post("/chat")
async def chat(request: ChatRequest):

    start_time = time.time()

    if request.streaming:
        response = StreamingResponse(
            stream_from_openai(request.llm, request.query), media_type="text/plain"
        )
    else:
        content = await chat_from_openai(request.llm, request.query)
        response = Response(content, media_type="text/plain")

    end_time = time.time()
    duration = end_time - start_time
    print(f"Response time: {duration} seconds")

    return response