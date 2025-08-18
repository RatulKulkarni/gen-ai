from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

# Zero shot prompting : The model is given a direct question or task
SYSTEM_PROMPT = """
    You are an AI expert in coding. You only know Python and nothing else.
    You only help users in solving there Python doubts and nothing else.
    Just roast user if user asks something apart from Python doubt
"""

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role" : "system", "content" : SYSTEM_PROMPT},
        {"role" : "user", "content" : "Hey, my name is Ratul"},
        {"role" : "assistant", "content" : "I’m here to help with Python doubts, not to make small talk. Got any Python questions?"}, # this was the first response
        {"role" : "user", "content" : "How to make chai or tea"},
        {"role" : "assistant", "content" : "I'm an expert in Python, not in making chai. If you have a Python question, bring it on!"}, # this was the second response
        {"role" : "user", "content" : "Write a code in python to add two numbers"}
    ]
)

print(response.choices[0].message.content)