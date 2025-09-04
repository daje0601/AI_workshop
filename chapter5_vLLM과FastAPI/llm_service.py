import os
import httpx
from openai import AsyncOpenAI
from dotenv import load_dotenv
from prompt import system_prompt

load_dotenv()

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
    url = f"https://api.runpod.ai/v2/{RUNPOD_ENDPOINT_ID}/runsync"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {RUNPOD_API_KEY}"
    }
    payload = {
        "input": {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": query}
            ]
        }
    }
    
    async with httpx.AsyncClient() as client:
        response = await client.post(url, headers=headers, json=payload, timeout=30.0)
    
    result = response.json()
    tokens = result["output"][0]["choices"][0]["tokens"]
    return "".join(tokens)