"""
Module for defining search tools used in the analysis.
"""

from langchain_community.tools.tavily_search import TavilySearchResults
from langchain.tools import Tool


class SearchTools:
    """Class responsible for creating and managing search tools."""

    @staticmethod
    def create_tavily_search() -> Tool:
        """
        Create and configure Tavily search tool.

        Returns:
            Tool: Configured search tool
        """
        tavily_search = TavilySearchResults(max_results=5)
        return Tool(
            name="Search",
            func=tavily_search.invoke,
            description="Useful for searching current information about AI models"
        )