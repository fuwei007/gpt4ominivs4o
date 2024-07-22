import os
from openai import OpenAI

os.environ['OPENAI_API_KEY'] = ''
## Set the API key
client = OpenAI()

model="gpt-4o-mini-2024-07-18"

completion = client.chat.completions.create(
  model=model,
  messages=[
    {"role": "system", "content": "You are a helpful assistant that helps me with my math homework!"},
    {"role": "user", "content": "Hello! Could you solve 20 x 5?"}
  ]
)
print("Assistant: " + completion.choices[0].message.content)
