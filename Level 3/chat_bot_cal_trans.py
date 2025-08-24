from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import Tool
from langchain.agents import AgentExecutor,create_react_agent
from langchain.prompts import ChatPromptTemplate 
from dotenv import load_dotenv
import os
load_dotenv()
from calculator_tools import *
from translator_tools import *

tools = [
    Tool(
        name="Add",  
        func=add_tool,  

        description="Useful for when you need to add numbers. Identify the two numbers and send to tool accordingly. Input should be two numbers: a and b, separated by a comma.",
    ),
    Tool(
        name="Subtract",  
        func=subtract_tool,  
        description="Useful for when you need to subtract two numbers. Input should be two numbers: a and b, separated by a comma.",
    ),
    Tool(
        name="Multiply",  
        func=multiply_tool,  
        description="Useful for when you need to multiply numbers. Input should be two numbers: a and b, separated by a comma.",
    ),
    Tool(
        name="Divide",  
        func=divide_tool,  
        description="Useful for when you need to divide two numbers. Input should be two numbers: a and b, separated by a comma.",
    ),
    Tool(
        name="Power",  
        func=power_tool,  
        description="Useful for when you need to raise a number to the power of another. Input should be two numbers: a and b, separated by a comma.",
    ),
    Tool(
        name="Square Root",  
        func=sqrt_tool,  
        description="Useful for when you need to find the square root of a number. Input should be a single non-negative number.",
    ),
    Tool(
        name="Modulus",  
        func=modulus_tool,  
        description="Useful for when you need to find the remainder of division between two numbers. Input should be two numbers: a and b, separated by a comma.",
    ),
    Tool(
        name="english_to_french",  
        func=eng_to_fren,  
        description="Useful for when you need to translate text from English to French. Input should be in the format: 'required_text'.",
    ),
    Tool(
        name="english_to_german",  
        func=eng_to_ger,  
        description="Useful for when you need to translate text from English to German. Input should be in the format: 'required_text'.",
    ),
    Tool(
        name="english_to_italian",  
        func=end_to_itly,  
        description="Useful for when you need to translate text from English to Italian. Input should be in the format: 'required_text'.",
    ),

]

tem_prompt = """
You are a helpful assistant. Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format to answer the question:

Question: the input question you must answer
Thought: you should always think about what to do. Do I need to use a tool? Yes or No?
Action: the action to take, should be one of [{tool_names}] if you need a tool or answer from your knowledge.
Action Input: the input to the action.
Observation: the result of the action.
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer.
Final Answer: the final answer to the original input question.


Begin!

Question: {input}

{agent_scratchpad}
"""


def main():
    """
    Sets up and runs a LangChain agent that can use a calculator tool.
    """

    llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash",api_key=os.getenv("GOOGLE_API_KEY"))

    prompt = ChatPromptTemplate.from_template(tem_prompt)

    agent = create_react_agent(llm, tools, prompt)


    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    print("LLM with Calculator Tool (Level 2)")
    print("Type 'quit' or 'exit' to stop.")
    print("-" * 50)

    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit"]:
            print("Goodbye! ")
            break
        
        if not user_input.strip():
            continue

        try:
            response = agent_executor.invoke({"input": user_input})
            print(f"Assistant: {response['output']}\n")
        except Exception as e:
            print(f"An error occurred: {e}")
        
        print("-" * 50)

if __name__ == "__main__":
    main()