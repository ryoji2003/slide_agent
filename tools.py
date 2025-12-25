import os 
from dotenv import load_dotenv
import getpass
from langchain_tavily import TavilySearch


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def get_search_tool(thema):
    tool = TavilySearch(
        max_results=5,
        topic="general",
        # include_answer=False,
        # include_raw_content=False,
        # include_images=False,
        # include_image_descriptions=False,
        # search_depth="basic",
        # time_range="day",
        # include_domains=None,
        # exclude_domains=None
    )

    result = tool.invoke({"query": thema})

    print(result)

if __name__ == "__main__":
    thema = input("あなたが作りたい資料のテーマを入力してください: ")
    get_search_tool(thema)