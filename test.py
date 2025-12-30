# "up_1qBaUUoYUJNdlcqzNdiU632V3uDr8"

from openai import OpenAI

client = OpenAI(
    api_key="up_1qBaUUoYUJNdlcqzNdiU632V3uDr8",
    base_url="https://api.upstage.ai/v1"
)

stream = client.chat.completions.create(
    model="solar-pro2",
    messages=[
        {
            "role": "user",
            "content": "Hi, how are you?"
        }
    ],
    reasoning_effort="high",
    stream=False,
)

print(stream.choices[0].message.content)
