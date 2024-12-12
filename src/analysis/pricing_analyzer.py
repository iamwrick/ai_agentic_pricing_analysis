"""
Main module for AI pricing analysis.
Coordinates agents, tasks, and analysis execution.
"""

from crewai import Crew
from ..agents.pricing_agents import PricingAgents
from ..tasks.pricing_tasks import PricingTasks
from ..tools.search_tools import SearchTools
from ..utils.logger import setup_logger
from ..utils.report_generator import ReportGenerator

logger = setup_logger(__name__)


class PricingAnalyzer:
    """Main class for conducting AI pricing analysis."""

    def __init__(self):
        """Initialize the pricing analyzer with necessary components."""
        self.search_tool = SearchTools.create_tavily_search()
        self.agents = PricingAgents(self.search_tool).get_all_agents()
        self.tasks = PricingTasks.get_all_tasks(self.agents)
        self.report_generator = ReportGenerator()

    def run_analysis(self) -> str:
        """
        Execute the complete pricing analysis.

        Returns:
            str: Generated analysis report
        """
        logger.debug("Starting analysis run")
        try:
            crew = Crew(
                agents=self.agents,
                tasks=self.tasks,
                verbose=True
            )

            result = crew.kickoff()
            return self.report_generator.generate_report(result)

        except Exception as e:
            logger.error(f"Error in analysis: {e}")
            raise