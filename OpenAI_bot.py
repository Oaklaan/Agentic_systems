
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

# Add your API key directly here
llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="api-key-here",
    temperature=0.7
)

def ai_assistant():
    print("🤖 Python Buddy: Hey! Nice to meet you.")
    print("Let's talk about Python. Type 'exit' to quit.")

    history = [
        SystemMessage(content="""
        You are a friendly AI assistant who talks like a human.
        Be natural, friendly, and conversational.
        Explain Python concepts simply with examples.
        Remember the conversation context.
        Focus mainly on Python programming.
        """ )
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
            history.append(AIMessage(content=response.content))
            print(f"\nPython Buddy: {response.content}")

        except Exception as e:
            history.pop()
            print(f"Sorry, something went wrong: {e}")

ai_assistant()