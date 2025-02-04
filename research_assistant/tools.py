from dotenv import load_dotenv
import os

from langchain_community.tools.reddit_search.tool import RedditSearchRun
from langchain_community.utilities.reddit_search import RedditSearchAPIWrapper
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper

load_dotenv()

wikipedia_tool = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
semantic_scholar_tool = SemanticScholarQueryRun()
reddit_tool = RedditSearchRun(
    api_wrapper=RedditSearchAPIWrapper(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
        user_agent=os.getenv("REDDIT_USER_AGENT")
    )
)

# Initialize tools
tools = [
    wikipedia_tool,
    reddit_tool,
    semantic_scholar_tool,
] 