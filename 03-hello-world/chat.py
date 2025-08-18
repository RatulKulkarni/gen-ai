from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role" : "user", "content" : "Who was the captain of 2011 Cricket World Cup winning team"}
    ]
)

print(response.choices[0].message.content)