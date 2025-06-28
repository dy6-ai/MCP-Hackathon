from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "combined": {
                "url": "http://localhost:8000/mcp",  # Combined server running here
                "transport": "streamable_http",
            }
        }
    )

    import os
    openai_key = os.getenv("OPENAI_API_KEY")
    if openai_key:
        os.environ["OPENAI_API_KEY"] = openai_key

    tools = await client.get_tools()
    model = ChatOpenAI(model="gpt-3.5-turbo")
    agent = create_react_agent(
        model, tools
    )

    # Example queries that will automatically select the right tools
    test_queries = [
        "What's 15 + 27?",
        "Calculate 8 * 9",
        "What's the weather in Tokyo?",
        "Subtract 50 from 100",
        "What is 25% of 200?",
        "Calculate 5 to the power of 3",
        "What's 100 divided by 4 and what's the weather in London?",
        "Add 10 and 20, then multiply by 3"
    ]

    for i, query in enumerate(test_queries, 1):
        print(f"\n--- Query {i}: {query} ---")
        try:
            response = await agent.ainvoke(
                {"messages": [{"role": "user", "content": query}]}
            )
            print("Response:", response['messages'][-1].content)
        except Exception as e:
            print(f"Error: {e}")

asyncio.run(main())
