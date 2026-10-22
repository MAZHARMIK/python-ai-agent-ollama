# standard library imports
import os

# Third-party imports
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

stream = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[{"role": "user", "content": "Explain what an API is in 100 words. No need to mention the number of words used."}],
    stream=True,
)

full_response = ""

for chunk in stream:
    if not chunk.choices:                       # some servers send chunks with no choices
        continue

    piece = chunk.choices[0].delta.content
    if piece:
        print(piece, end="", flush=True) #streaming
        full_response += piece


print("\nFull response:")
print(full_response) #I will send this to LLM for history
