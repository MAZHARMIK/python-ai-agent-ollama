from openai import OpenAI
import os
import numpy
from dotenv import load_dotenv

load_dotenv() #by default looks for .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)


def get_embedding(text):
    response = client.embeddings.create(
        model=os.getenv("EMBED_MODEL"),
        input=text,
    )
    return response.data[0].embedding


def cosine_similarity(A, B):
    dot_prod = numpy.dot(A, B)
    norm_a = numpy.linalg.norm(A)
    norm_b = numpy.linalg.norm(B)
    return dot_prod / (norm_a * norm_b)


text1 = "Python is a programming language"
text2 = "Python is used to write AI related code snippets"
text3 = "I love eating Apples every morning"

embedding1 = get_embedding(text1)
embedding2 = get_embedding(text2)
embedding3 = get_embedding(text3)

similarity12 = cosine_similarity(embedding1, embedding2)
similarity13 = cosine_similarity(embedding1, embedding3)

print("Similarity between text1 and text2:", f"{similarity12:.2f}")
print("Similarity between text1 and text3:", f"{similarity13:.2f}")
