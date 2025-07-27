print("🤖 Simple Chatbot Ready! Type 'bye' to quit.")

while True:
    user = input("You: ").lower()

    if user == "bye":
        bot_response = "Goodbye! 👋"
        print("Bot:", bot_response)
        # ✅ Save the final message before quitting
        with open("chat_history.txt", "a") as f:
            f.write(f"You: {user}\nBot: {bot_response}\n\n")
        break

    elif "hello" in user or "hi" in user:
        bot_response = "Hello! How can I help you today?"
    elif "how are you" in user:
        bot_response = "I'm just code, but I'm doing great! 😄"
    elif "your name" in user:
        bot_response = "I'm a simple chatbot made in Python."
    elif "help" in user:
        bot_response = "You can ask me things like 'hello', 'how are you', or say 'bye' to exit."
    else:
        bot_response = "Sorry, I didn't understand that."

    print("Bot:", bot_response)

    # ✅ Add this block inside the while loop (after print)
    with open("chat_history.txt", "a") as f:
        f.write(f"You: {user}\nBot: {bot_response}\n\n")
