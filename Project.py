import openai
import os

# Get API key from environment variable
openai.api_key = os.getenv("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")

def chat_with_gpt(user_input):
    client = openai.Client(api_key=openai.api_key)  # Explicitly pass API key
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_input}]
    )
    return response.choices[0].message.content  

user_input = input("You: ")
response = chat_with_gpt(user_input)
print("GPT:", response)
