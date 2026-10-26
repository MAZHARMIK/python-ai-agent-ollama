from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv() #by default looks for .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

response = client.embeddings.create(
    model=os.getenv("EMBED_MODEL"),
    input=["I am a good boy", "Python is a good language", "He is a good coder"],
)

for i, emb in enumerate(response.data):
    print(f"Embedding {i} length: {len(emb.embedding)}")
    print(emb.embedding[:5])
