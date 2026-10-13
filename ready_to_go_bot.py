
import random
import ast
import re


def ai_assistant():
    print("=" * 50)
    print("       🤖 PYTHON SMART ASSISTANT")
    print("=" * 50)
    print("Hey! I'm here to help you learn Python.")
    print("Ask me questions, explore examples, or debug simple code.")
    print("Commands: help, clear, exit")
    print("=" * 50)

    name = None
    last_topic = None

    knowledge = {
        "variable": {
            "keywords": ["variable", "variables"],
            "answer": (
                "A variable is like a box that stores information.\n"
                "Example:\n"
                "age = 21\n"
                "name = 'Krushna'\n\n"
                "Here, age stores a number and name stores text.\n"
                "You can use these values later in your program."
            )
        },

        "loop": {
            "keywords": ["loop", "loops", "iteration", "iterate"],
            "answer": (
                "A loop repeats a block of code.\n\n"
                "For loop:\n"
                "for i in range(3):\n"
                "    print(i)\n\n"
                "Output:\n"
                "0\n1\n2\n\n"
                "A for loop is useful when repeating a task.\n"
                "A while loop repeats while its condition is True."
            )
        },

        "function": {
            "keywords": ["function", "functions", "def"],
            "answer": (
                "A function is a reusable block of code.\n\n"
                "Example:\n"
                "def greet(name):\n"
                "    return 'Hello ' + name\n\n"
                "print(greet('Alex'))\n\n"
                "Output: Hello Alex\n\n"
                "Functions help you organize code and avoid repetition."
            )
        },

        "list": {
            "keywords": ["list", "lists", "array"],
            "answer": (
                "A list stores multiple items in one variable.\n\n"
                "numbers = [10, 20, 30]\n"
                "numbers.append(40)\n"
                "print(numbers)\n\n"
                "Output: [10, 20, 30, 40]\n\n"
                "Lists are ordered and can be changed after creation."
            )
        },

        "dictionary": {
            "keywords": ["dictionary", "dict", "key value"],
            "answer": (
                "A dictionary stores data as key-value pairs.\n\n"
                "student = {'name': 'Alex', 'age': 21}\n"
                "print(student['name'])\n\n"
                "Output: Alex\n\n"
                "Dictionaries are useful when data has named fields."
            )
        },

        "tuple": {
            "keywords": ["tuple", "tuples"],
            "answer": (
                "A tuple stores multiple items like a list, "
                "but it cannot be modified after creation.\n\n"
                "point = (10, 20)\n"
                "print(point[0])\n\n"
                "Output: 10"
            )
        },

        "set": {
            "keywords": ["set", "sets"],
            "answer": (
                "A set stores unique values and removes duplicates.\n\n"
                "numbers = {1, 2, 2, 3}\n"
                "print(numbers)\n\n"
                "Output: {1, 2, 3}\n\n"
                "Sets are useful for removing duplicates."
            )
        },

        "condition": {
            "keywords": ["if statement", "condition", "conditional",
                         "if else", "elif"],
            "answer": (
                "Conditions let your program make decisions.\n\n"
                "age = 18\n"
                "if age >= 18:\n"
                "    print('Adult')\n"
                "else:\n"
                "    print('Minor')\n\n"
                "Output: Adult\n\n"
                "Python executes the matching branch."
            )
        },

        "class": {
            "keywords": ["class", "classes", "object", "oops"],
            "answer": (
                "A class is a blueprint for creating objects.\n\n"
                "class Dog:\n"
                "    def __init__(self, name):\n"
                "        self.name = name\n\n"
                "dog = Dog('Buddy')\n"
                "print(dog.name)\n\n"
                "Output: Buddy\n\n"
                "The object stores its own name."
            )
        },

        "exception": {
            "keywords": ["exception", "exceptions", "try except",
                         "error handling"],
            "answer": (
                "Exception handling lets you deal with errors gracefully.\n\n"
                "try:\n"
                "    number = int('abc')\n"
                "except ValueError:\n"
                "    print('Please enter a valid number')\n\n"
                "Instead of stopping unexpectedly, the program handles "
                "the conversion error."
            )
        },

        "file": {
            "keywords": ["file handling", "read file", "write file"],
            "answer": (
                "Python can read and write files.\n\n"
                "with open('notes.txt', 'w') as file:\n"
                "    file.write('Hello Python!')\n\n"
                "This creates or replaces notes.txt and writes text to it.\n"
                "The with statement closes the file automatically."
            )
        },

        "module": {
            "keywords": ["module", "modules", "import", "library"],
            "answer": (
                "A module is a Python file containing reusable code.\n\n"
                "import math\n"
                "print(math.sqrt(25))\n\n"
                "Output: 5.0\n\n"
                "The math module provides mathematical functions."
            )
        }
    }

    def normalize(text):
        return re.sub(r"[^a-z0-9_ ]", " ", text.lower()).strip()

    def find_topic(question):
        text = normalize(question)

        # Match specific phrases before shorter keywords.
        for topic, data in knowledge.items():
            for keyword in sorted(data["keywords"],
                                 key=len, reverse=True):
                if re.search(
                    r"(?<!\w)" + re.escape(keyword) + r"(?!\w)",
                    text
                ):
                    return topic

        return None

    def debug_code(code):
        try:
            ast.parse(code)
            return (
                "Your code has valid Python syntax.\n"
                "This doesn't guarantee it will run correctly, "
                "because runtime errors may still occur."
            )
        except SyntaxError as error:
            return (
                f"Syntax error on line {error.lineno}: "
                f"{error.msg}\n"
                "Check indentation, brackets, colons, and quotation marks."
            )

    while True:
        try:
            question = input("\nYou: ").strip()
        except (KeyboardInterrupt, EOFError):
            print("\nAI: Goodbye! Keep learning Python. 👋")
            break

        if not question:
            print("AI: Take your time! What would you like to learn?")
            continue

        text = normalize(question)

        if text in ["exit", "quit", "bye", "goodbye"]:
            print("AI: It was great chatting with you. Goodbye! 👋")
            break

        elif text == "help":
            print(
                "\nAI: Here is what I can help with:\n"
                "- Python basics and examples\n"
                "- Variables, loops, functions, and collections\n"
                "- Classes and exception handling\n"
                "- Simple Python syntax checking\n"
                "- Follow-up questions about the last topic\n"
                "- Greetings and small talk\n"
                "\nTry: Explain functions with an example."
            )

        elif text == "clear":
            name = None
            last_topic = None
            print("AI: Fresh start! What would you like to discuss?")
            continue

        elif any(word in text.split()
                 for word in ["hello", "hi", "hey", "namaste"]):
            replies = [
                "Hey! 😊 What are we learning today?",
                "Hello! Ready to explore some Python?",
                "Hi there! Ask me anything about Python basics."
            ]
            print("AI:", random.choice(replies))

        elif "your name" in text or "who are you" in text:
            print(
                "AI: I'm your Python Smart Assistant. "
                "I can explain concepts, show examples, "
                "and check Python syntax."
            )

        elif "my name is" in text:
            name = question.split("my name is", 1)[-1].strip()
            if not name:
                name = question.split("My name is", 1)[-1].strip()
            print(f"AI: Nice to meet you, {name}!")

        elif text in ["what is my name", "do you know my name"]:
            if name:
                print(f"AI: You told me your name is {name}.")
            else:
                print("AI: You haven't told me your name yet.")

        elif any(phrase in text for phrase in
                 ["another example", "explain more", "tell me more",
                  "give example", "what about it", "explain again"]):
            if last_topic:
                print("AI:", knowledge[last_topic]["answer"])
            else:
                print("AI: Which Python topic would you like me to explain?")

        elif "debug" in text or "check my code" in text:
            print("AI: Paste your Python code after this prompt.")
            code = input("Code: ")
            print("AI:", debug_code(code))

        elif text.startswith("what is the output"):
            print(
                "AI: Paste the code you'd like to check using "
                "the 'debug' command. I can check syntax, "
                "but I don't execute the code."
            )

        elif any(word in text.split()
                 for word in ["thanks", "thank", "thankyou"]):
            print("AI: You're welcome! Happy to help. 😊")

        elif "how are you" in text:
            print("AI: I'm running smoothly! How can I help you today?")

        elif "difference between" in text:
            if "list" in text and "tuple" in text:
                print(
                    "AI: A list is mutable, so you can change it. "
                    "A tuple is immutable, so you cannot change its items "
                    "after creation.\nExample: [1, 2] versus (1, 2)."
                )
            elif "for" in text and "while" in text:
                print(
                    "AI: A for loop is commonly used to iterate over "
                    "a sequence. A while loop repeats while a condition "
                    "remains True."
                )
            else:
                print(
                    "AI: Please name both concepts clearly. "
                    "For example: difference between list and tuple."
                )

        else:
            topic = find_topic(question)

            if topic:
                last_topic = topic
                print("AI:", knowledge[topic]["answer"])

            else:
                print(
                    "AI: I haven't learned how to answer that question yet.\n"
                    "Try asking about variables, loops, functions, lists, "
                    "dictionaries, tuples, sets, classes, or modules.\n"
                    "You can also type 'help' to see my capabilities."
                )


if __name__ == "__main__":
    ai_assistant()
