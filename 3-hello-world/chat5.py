# Self Consistency Prompting
# Persona based Prompting

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

# Persona based Prompting

SYSTEM_PROMPT = """
    You are an AI Persona of Ratul. You have to ans to every question as if you are
    Ratul and sound natural and human tone. Use the below examples to understand how Ratul talks
    and a background about him.

    Background
    

    Examples
     Atleast 50-80 examples
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        { "role": "system", "content": SYSTEM_PROMPT },
        { "role": "user", "content": "Hey, My name is Ratul"},
        
    ]
)

print(response.choices[0].message.content)