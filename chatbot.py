import nltk
import random
import string

nltk.download('punkt')

greetings = ["hi", "hello", "hey", "hola", "greetings"]
responses = ["Hi there!", "Hello!", "Hey!", "Nice to meet you!", "Hi, how can I help?"]

farewells = ["bye", "goodbye", "see you", "exit", "quit"]
farewell_responses = ["Goodbye!", "See you later!", "Bye!", "Take care!"]

def get_response(user_input):
    user_input = user_input.lower()
    tokens = nltk.word_tokenize(user_input)

    if any(word in tokens for word in greetings):
        return random.choice(responses)
    elif any(word in tokens for word in farewells):
        return random.choice(farewell_responses)
    elif "help" in tokens:
        return "Sure! You can ask me about greetings, weather, or say bye to exit."
    elif "weather" in tokens:
        return "The weather is nice and sunny!"
    else:
        return "I'm not sure I understand. Can you rephrase?"

def chatbot():
    print("ChatBot: Hi! I'm your friendly chatbot. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("ChatBot:", response)
        if response in farewell_responses:
            break

chatbot()
