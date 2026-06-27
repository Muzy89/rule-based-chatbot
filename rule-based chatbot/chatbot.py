from responses import responses

print("=" * 45)
print("        Welcome to RuleBot")
print("=" * 45)
print("Type 'help' to see available commands.")
print("Type 'exit' to quit.\n")

while True:

    user = input("You: ").lower().strip()

    if user == "exit":
        print("Bot: Goodbye!")
        break

    elif user == "help":
        print("\nAvailable Questions")
        print("---------------------------")
        print("hello")
        print("hi")
        print("hey")
        print("how are you")
        print("your name")
        print("who made you")
        print("python")
        print("ai")
        print("time")
        print("bye")
        print()

    elif user in responses:
        print("Bot:", responses[user])

    elif "weather" in user:
        print("Bot: Sorry, I don't have internet access to check the weather.")

    elif "age" in user:
        print("Bot: I don't have an age. I'm just a Python program.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "good morning" in user:
        print("Bot: Good Morning! Hope you have a productive day!")

    elif "good night" in user:
        print("Bot: Good Night! Sweet dreams!")

    elif "joke" in user:
        print("Bot: Why do programmers prefer Python?")
        print("Bot: Because it's easy to understand!")

    else:
        print("Bot: Sorry, I don't understand that. Type 'help' to see available questions.")