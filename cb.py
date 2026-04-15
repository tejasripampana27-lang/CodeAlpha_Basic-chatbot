print("🤖 Smart Chatbot")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I assist you?")
    
    elif user_input in ["how are you", "how r u"]:
        print("Bot: I'm doing great! 😊 What about you?")
    
    elif user_input in ["what is your name", "your name"]:
        print("Bot: I'm your Python chatbot 🤖")
    
    elif "python" in user_input:
        print("Bot: Python is a powerful and easy programming language!")
    
    elif user_input in ["thanks", "thank you"]:
        print("Bot: You're welcome! 😊")
    
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day 👋")
        break
    
    else:
        print("Bot: Hmm... I didn't understand that. Try something else!")