import os
import httpx
from openai import AsyncOpenAI
from dotenv import load_dotenv
from prompt import system_prompt

load_dotenv("./env")

# 클라이언트 초기화
openai_client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
RUNPOD_ENDPOINT_ID = os.getenv("RUNPOD_ENDPOINT_ID", "ul8u0wp2gc352x")
RUNPOD_API_KEY = os.getenv("RUNPOD_API_KEY")


# OpenAI 함수들
async def chat_openai(model: str, query: str, streaming: bool = False):
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
    
    if streaming:
        stream = await openai_client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True
        )
        async def generator():
            async for chunk in stream:
                if chunk.choices[0].delta.content:
                    content = chunk.choices[0].delta.content
                    print(f"Streaming chunk: {content}")
                    yield content
        return generator()
    else:
        completion = await openai_client.chat.completions.create(
            model=model,
            messages=messages
        )
        return completion.choices[0].message.content


# RunPod 함수
async def chat_runpod(query: str):
    # OpenAI 호환 클라이언트를 사용하여 RunPod에 연결
    runpod_client = AsyncOpenAI(
        api_key=RUNPOD_API_KEY,
        base_url=f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/openai/v1"
    )
    
    MODEL_NAME = "iamjoon/llama3-8b-finance-analyzer"
    
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": query}
    ]
    
    try:
        response = await runpod_client.chat.completions.create(
            model=MODEL_NAME,
            messages=messages,
            temperature=0,
            stop=["\n<|end_of_text|>", "<|eot_id|>"]
        )
        
        # 전체 응답 내용을 반환
        return response.choices[0].message.content
    except Exception as e:
        print(f"RunPod API Error: {e}")
        return f"Error: {str(e)}"