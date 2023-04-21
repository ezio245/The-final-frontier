import openai_secret_manager
import openai
import json

# Get your OpenAI API key from the environment variables
secrets = openai_secret_manager.get_secret("openai")

# Set up the OpenAI API client
openai.api_key = secrets["api_key"]

# Define a function that sends user input to the OpenAI API and returns the response
def get_openai_response(input_text):
    response = openai.Completion.create(
        engine="davinci", # Choose a language model to use
        prompt=input_text,
        max_tokens=50, # Set the maximum number of tokens to generate in the response
        n=1, # Set the number of responses to generate
        stop=None, # Set stopping criteria for generation (i.e. stop when a certain phrase is generated)
        temperature=0.5 # Set the "creativity" of the model (higher temperature = more creative, but potentially less coherent)
    )

    return response.choices[0].text.strip()

# Define a function that handles user input and sends it to the OpenAI API
def handle_user_input(input_text):
    # Check if the user input is a greeting
    if "hello" in input_text.lower() or "hi" in input_text.lower():
        return "Hi there! How can I assist you today?"

    # Check if the user input is a question
    if "?" in input_text:
        return get_openai_response(input_text)

    # Otherwise, respond with a default message
    return "I'm sorry, I didn't understand. Can you please rephrase that?"

# Define a function that runs the chatbot
def run_chatbot():
    while True:
        user_input = input("User: ")
        response = handle_user_input(user_input)
        print("Chatbot:", response)

# Run the chatbot
run_chatbot()

