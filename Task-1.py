Task -1
print("Welcome to ChatBot")

while True:
    user_input = input("You: ").lower()

    if "hey" in user_input or "hi" in user_input:
        print("ChatBot: Hey! How it's going on?")

    elif "how are you?" in user_input:
        print("ChatBot: I'm doing great, thanks for asking! How about you?")

    elif "what is your name?" in user_input:
        print("ChatBot: I'm a simple rule-based AI ChatBot. You can call me anything you like!.Do you want any special name for myself when i chat with you?")

    elif "weather" in user_input:
        print("ChatBot: I can't check live weather yet, but I can tell you it's always sunny in my code.")

    elif "bye" in user_input or "exit" in user_input:
        print("ChatBot: Goodbye! Have a great day! Take care")
        break

    else:
        print("ChatBot: Sorry, I didn't understand that. Can you rephrase?")
