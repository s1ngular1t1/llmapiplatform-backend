import os
import asyncio
from openai import AsyncOpenAI

client = AsyncOpenAI(
    # This is the default and can be omitted
    api_key="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",
)


async def chat_gpt_test() -> None:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "give me a math problem to solve",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content


async def generate_response(prompt: str) -> str:
    chat_completion = await client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "give me a shoping list",
            }
        ],
        model="gpt-3.5-turbo",
    )
    print(chat_completion.choices[0].message.content)
    return chat_completion.choices[0].message.content

