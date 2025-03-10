import random

responses = {
    "hello": ["Hi there!", "Hello!", "Hey!", "Hi! How can I help?"],
    "how are you": ["I’m good, thanks!", "Doing great! How about you?", "I’m just a bot, but I’m fine!"],
    "bye": ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    "your name": ["I’m a chatbot!", "Just call me ChatBot.", "I’m your friendly bot."],
    "default": ["Sorry, I don’t understand.", "Can you rephrase that?", "I’m not sure what you mean."]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    return random.choice(responses["default"])

print("Chatbot: Hello! Type ‘bye’ to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Chatbot:", chatbot_response(user_input))
        break
    print("Chatbot:", chatbot_response(user_input))