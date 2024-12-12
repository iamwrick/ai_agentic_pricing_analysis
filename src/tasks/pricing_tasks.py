"""
Module for defining AI pricing analysis tasks.
Contains task definitions for different types of analysis.
"""

from crewai import Task
from typing import List
from crewai import Agent


class PricingTasks:
    """Class responsible for creating and managing analysis tasks."""

    @staticmethod
    def create_pricing_research(agent: Agent) -> Task:
        """
        Create pricing research task.

        Args:
            agent (Agent): Agent to perform the task

        Returns:
            Task: Configured pricing research task
        """
        return Task(
            description="""Research and compile current pricing information...""",
            agent=agent,
            expected_output="""A detailed pricing comparison table..."""
        )

    @staticmethod
    def create_technical_research(agent: Agent) -> Task:
        """Create technical research task"""
        return Task(
            description="""Research technical specifications...""",
            agent=agent,
            expected_output="""A technical comparison matrix..."""
        )

    @staticmethod
    def create_market_analysis(agent: Agent) -> Task:
        """Create market analysis task"""
        return Task(
            description="""Analyze current market positioning...""",
            agent=agent,
            expected_output="""A comprehensive market analysis report..."""
        )

    @classmethod
    def get_all_tasks(cls, agents: List[Agent]) -> List[Task]:
        """
        Create and return all required tasks.

        Args:
            agents (List[Agent]): List of agents to assign to tasks

        Returns:
            List[Task]: List of all created tasks
        """
        return [
            cls.create_pricing_research(agents[0]),
            cls.create_technical_research(agents[1]),
            cls.create_market_analysis(agents[2])
        ]