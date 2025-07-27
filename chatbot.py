from datetime import datetime

print("🤖 Simple Chatbot Ready! Type 'bye' to quit.")

while True:
    user = input("You: ").lower()
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # ⏰ Get current timestamp

    if user == "bye":
        bot_response = "Goodbye! 👋"
        print("Bot:", bot_response)
        with open("chat_history.txt", "a") as f:
            f.write(f"[{time_now}] You: {user}\n[{time_now}] Bot: {bot_response}\n\n")
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

    # ✅ Save with timestamp
    with open("chat_history.txt", "a") as f:
        f.write(f"[{time_now}] You: {user}\n[{time_now}] Bot: {bot_response}\n\n")
