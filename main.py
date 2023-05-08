import openai
import time

openai.api_key = "Your_api_key"

prompt = "Hello, I'm a chatbot. What can I help you with today?"

chat_history = openai.Completion.create(
    engine="text-davinci-002",
    prompt=prompt,
    temperature=0.7,
    max_tokens=1024,
    n=1,
    stop=None,
    timeout=20,
)

def generate_response(prompt, user_input):
    prompt += f"\nUser: {user_input}\nChatbot:"

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        n=1,
        stop=None,
        timeout=20,
    )

    message = response.choices[0].text.strip()

    return message

while True:
    user_input = input("You: ")

    if user_input.lower() == "bye":
        print("Chatbot: Goodbye!")
        break

    response = generate_response(prompt, user_input)

    print(f"Chatbot: {response}")

    prompt += f"\nUser: {user_input}\nChatbot: {response}"
    time.sleep(1)
