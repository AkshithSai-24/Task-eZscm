# chatbot.py
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv


load_dotenv()


sys_prompt = """
You are a helpful and smart assistant. Your primary goal is to answer user questions clearly and thoughtfully with Tempearatue=0.2 .

Follow these rules strictly:
1.  Think Step-by-Step: Before providing an answer, break down the user's question and think through the steps required to answer it. Start your response with a "Thinking..." block that outlines your thought process.
2.  Clear and Structured Output: Present your final answer in a clean, easy-to-read format. Use lists or numbered steps where appropriate.
3.  CRITICAL RULE: No Math Calculations: If the user asks you to perform any mathematical calculation (e.g., addition, subtraction, multiplication, division), you MUST refuse. Do not provide the numerical answer. Instead, you must politely state that you are not equipped to handle math and suggest they use a "calculator tool". 

Example of refusing a math question:
User: What is 5 * 8?
Assistant:
Thinking...
1. The user is asking a direct math question.
2. My instructions state I must refuse to answer math questions.
3. I need to inform the user that I can't do math and suggest a calculator tool.

I am not equipped to perform mathematical calculations. Please use a calculator tool to find the answer for "5 * 8".
"""



def get_llm_response(user_prompt: str, model):
    """
    Sends the user's prompt to the LLM and gets a response. [cite: 9]

    Args:
        user_prompt: The question from the user.
        model: The configured GenerativeModel instance.

    Returns:
        The text response from the LLM.
    """
    try:
        # Combine the system prompt with the user's question for guided output
        full_prompt = [("system", sys_prompt), ("user", user_prompt)]
        response = model.invoke(full_prompt)
        return response.content
    except Exception as e:
        return f"An error occurred while communicating with the API: {e}"

def main():
    """
    Main function to run the CLI chatbot application.
    """
    try:
        model = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash",api_key=os.getenv("GOOGLE_API_KEY"))
        print(" LLM-Only Smart Assistant (Level 1)")
        print("Ask me anything! Type 'quit' or 'exit' to stop.")
        print("-" * 50)

        while True:
            user_input = input("You: ")
            if user_input.lower() in ["quit", "exit"]:
                print("Goodbye! ")
                break
            
            if not user_input.strip():
                continue

            response = get_llm_response(user_input, model)
            print(f"\nAssistant:\n{response}\n")
            print("-" * 50)
            

    except ValueError as ve:
        print(f"Configuration Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()