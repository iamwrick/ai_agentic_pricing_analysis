"""
Module for defining AI pricing analysis agents.
Contains agent definitions for pricing, technical, and market analysis.
"""

from crewai import Agent
from typing import List
from langchain.tools import Tool


class PricingAgents:
    """
    Class responsible for creating and managing different types of analysis agents.
    """

    def __init__(self, search_tool: Tool):
        """
        Initialize PricingAgents with a search tool.

        Args:
            search_tool (Tool): The search tool to be used by agents
        """
        self.search_tool = search_tool

    def create_pricing_analyst(self) -> Agent:
        """
        Create a pricing analysis agent.

        Returns:
            Agent: Configured pricing analyst agent
        """
        return Agent(
            role='AI Pricing Analyst',
            goal='Gather and analyze current pricing structures of Anthropic and OpenAI models',
            backstory="""You are an expert in AI model pricing and licensing. Your task is to 
            search and find the most current pricing information for AI models from OpenAI and 
            Anthropic.""",
            tools=[self.search_tool],
            verbose=True
        )

    def create_technical_analyst(self) -> Agent:
        """Create technical analysis agent"""
        return Agent(
            role='AI Technical Analyst',
            goal='Research and compare technical capabilities and their cost implications',
            backstory="""You are a technical analyst specialized in AI model evaluation.""",
            tools=[self.search_tool],
            verbose=True
        )

    def create_market_analyst(self) -> Agent:
        """Create market strategy agent"""
        return Agent(
            role='AI Market Strategy Analyst',
            goal='Research current market positioning and pricing strategies',
            backstory="""You are a strategic analyst focused on AI market dynamics.""",
            tools=[self.search_tool],
            verbose=True
        )

    def get_all_agents(self) -> List[Agent]:
        """
        Create and return all required agents.

        Returns:
            List[Agent]: List of all created agents
        """
        return [
            self.create_pricing_analyst(),
            self.create_technical_analyst(),
            self.create_market_analyst()
        ]