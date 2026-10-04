from openai import OpenAI
from dotenv import load_dotenv
import os

# Load the API key from .env
load_dotenv()

# Create connection with OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

print("====================================")
print("        🤖 AI STUDY BUDDY")
print("====================================")

while True:

    print("\nChoose an option:")
    print("1. Ask a question")
    print("2. Explain a topic")
    print("3. Create a quiz")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    # Option 1 - Ask a question
    if choice == "1":

        question = input("\nWhat is your question? ")

        response = client.responses.create(
            model="gpt-6-luna",
            input=f"""
You are an AI Study Buddy.

Answer the student's question clearly and simply.
Use examples if necessary.

Student question:
{question}
"""
        )

        print("\n🤖 AI Study Buddy:")
        print(response.output_text)

    # Option 2 - Explain a topic
    elif choice == "2":

        topic = input("\nEnter the topic you want to learn: ")

        response = client.responses.create(
            model="gpt-6-luna",
            input=f"""
You are an AI Study Buddy.

Explain the following topic to a college student
in very simple language.

Topic:
{topic}

Include:
1. Simple definition
2. How it works
3. Example
4. Important points
"""
        )

        print("\n🤖 AI Study Buddy:")
        print(response.output_text)

    # Option 3 - Create a quiz
    elif choice == "3":

        topic = input("\nEnter the topic for the quiz: ")

        response = client.responses.create(
            model="gpt-6-luna",
            input=f"""
You are an AI Study Buddy.

Create a short quiz for a college student
about the topic below.

Topic:
{topic}

Create 5 multiple-choice questions.
Give 4 options for each question.
Do not reveal the answers immediately.
"""
        )

        print("\n📝 Quiz:")
        print(response.output_text)

    # Option 4 - Exit
    elif choice == "4":

        print("\nGood luck with your studies! 👋")
        break

    # Invalid choice
    else:

        print("\n❌ Please enter a number between 1 and 4.")