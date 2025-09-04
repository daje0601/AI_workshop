
import os
from openai import AsyncOpenAI
from dotenv import load_dotenv

from prompt import system_prompt

load_dotenv()
 


# 클라이언트를 한 번만 생성
client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def stream_from_openai(model: str, query: str):
    print(f"Starting stream with model: {model}, query: {query}")
    stream = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": query}
            ],
        stream=True
    )
    async for chunk in stream:
        if chunk.choices[0].delta.content:
            content = chunk.choices[0].delta.content
            yield content

async def chat_from_openai(model: str, query: str):
    completion = await client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt}, 
            {"role": "user", "content": query}
            ]
    )
    return completion.choices[0].message.content

