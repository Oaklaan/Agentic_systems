
def ai_assistant():
    print("🤖 Python Task Assistant")
    print("Ask Python questions or type 'exit' to quit.")

    while True:
        question = input("\nYou: ").lower().strip()

        if question == "exit":
            print("AI: Goodbye!")
            break

        elif "variable" in question:
            print("AI: A variable stores a value, e.g., x = 10.")

        elif "loop" in question:
            print("AI: A loop repeats code. Python has for and while loops.")

        elif "function" in question:
            print("AI: A function is reusable code defined using def.")

        elif "list" in question:
            print("AI: A list stores multiple items, e.g., [1, 2, 3].")

        else:
            print("AI: I specialize in Python basics. Ask about variables, loops, functions, or lists.")


ai_assistant()