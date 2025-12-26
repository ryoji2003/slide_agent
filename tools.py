import os 
from dotenv import load_dotenv
import getpass
from langchain_tavily import TavilySearch


load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")


def get_search_tool():
    tool = TavilySearch(
        max_results=3,
        #topic="general",
        # include_answer=False,
        # include_raw_content=False,
        # include_images=False,
        # include_image_descriptions=False,
        # search_depth="basic",
        # time_range="day",
        # include_domains=None,
        # exclude_domains=None
    )

    return tool

if __name__ == "__main__":
    tool = get_search_tool()
    print(tool.run("What is Tavily???"))
    