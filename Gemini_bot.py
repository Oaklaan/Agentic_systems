
from getpass import getpass

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Enter your API key securely
api_key = getpass("Enter your Gemini API key: ").strip()

if not api_key:
    raise ValueError("API key cannot be empty.")

# Configure the AI model
llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=api_key,
    temperature=0.7
)


def ai_assistant():
    print("\n🤖 Python Buddy: Hey! Nice to meet you.")
    print("Ask me Python questions or type 'exit' to quit.")

    history = [
        SystemMessage(
            content=(
                "You are Python Buddy, a friendly AI assistant. "
                "Explain Python concepts in simple, natural language. "
                "Give examples when useful. "
                "Remember the conversation context and focus mainly "
                "on Python programming."
            )
        )
    ]

    while True:
        question = input("\nYou: ").strip()

        if question.lower() == "exit":
            print("Python Buddy: See you soon! Take care! 👋")
            break

        if not question:
            continue

        history.append(HumanMessage(content=question))

        try:
            response = llm.invoke(history)

            history.append(response)

            print(f"\nPython Buddy: {response.text}")

        except Exception as e:
            # Remove the unanswered user message
            history.pop()
            print(f"\nSorry, something went wrong: {e}")


if __name__ == "__main__":
    ai_assistant()
