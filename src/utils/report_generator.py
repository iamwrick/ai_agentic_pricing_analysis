"""
Report generation module.
Handles formatting and generation of analysis reports.
"""

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional
import json
from .logger import setup_logger

logger = setup_logger(__name__)


class ReportGenerator:
    """Class responsible for generating and formatting analysis reports."""

    def __init__(self, output_dir: Optional[str] = None):
        """
        Initialize ReportGenerator.

        Args:
            output_dir (Optional[str]): Directory for saving reports
        """
        self.output_dir = Path(output_dir) if output_dir else Path("reports")
        self.output_dir.mkdir(exist_ok=True)
        self.logger = logger

    def generate_report(self, analysis_result: str) -> str:
        """
        Generate a formatted report from analysis results.

        Args:
            analysis_result (str): Raw analysis results

        Returns:
            str: Formatted report
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report = f"""
            AI Model Pricing Analysis Report
            ==============================
            Generated on: {timestamp}

            Executive Summary
            ----------------
            This report provides a comprehensive analysis of AI model pricing,
            technical capabilities, and market positioning for major AI providers.

            Analysis Results
            ---------------
            {analysis_result}

            Methodology
            -----------
            This analysis was conducted using automated intelligence gathering
            and analysis tools, with data verified from multiple sources.
            """

            self._save_report(report, timestamp)
            return report

        except Exception as e:
            self.logger.error(f"Error generating report: {e}")
            raise

    def _save_report(self, report: str, timestamp: str) -> None:
        """
        Save the report to a file.

        Args:
            report (str): Generated report
            timestamp (str): Timestamp for file naming
        """
        try:
            filename = f"ai_pricing_analysis_{timestamp.replace(' ', '_').replace(':', '-')}.txt"
            file_path = self.output_dir / filename

            with open(file_path, 'w') as f:
                f.write(report)

            self.logger.info(f"Report saved to {file_path}")

        except Exception as e:
            self.logger.error(f"Error saving report: {e}")
            raise

    def generate_json_report(self, analysis_data: Dict[str, Any]) -> str:
        """
        Generate a JSON-formatted report.

        Args:
            analysis_data (Dict[str, Any]): Analysis data in dictionary format

        Returns:
            str: JSON-formatted report
        """
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            report_data = {
                "timestamp": timestamp,
                "type": "AI Model Pricing Analysis",
                "data": analysis_data
            }

            json_report = json.dumps(report_data, indent=4)

            # Save JSON report
            filename = f"ai_pricing_analysis_{timestamp.replace(' ', '_').replace(':', '-')}.json"
            file_path = self.output_dir / filename

            with open(file_path, 'w') as f:
                f.write(json_report)

            self.logger.info(f"JSON report saved to {file_path}")
            return json_report

        except Exception as e:
            self.logger.error(f"Error generating JSON report: {e}")
            raise

    def format_pricing_table(self, pricing_data: Dict[str, Dict[str, Any]]) -> str:
        """
        Format pricing data into a readable table.

        Args:
            pricing_data (Dict[str, Dict[str, Any]]): Pricing data to format

        Returns:
            str: Formatted pricing table
        """
        try:
            table = "Model Pricing Comparison\n"
            table += "=" * 80 + "\n"
            table += f"{'Model':<20} {'Input Price':<15} {'Output Price':<15} {'Context Window':<15}\n"
            table += "-" * 80 + "\n"

            for model, data in pricing_data.items():
                table += f"{model:<20} {data.get('input_price', 'N/A'):<15} "
                table += f"{data.get('output_price', 'N/A'):<15} "
                table += f"{data.get('context_window', 'N/A'):<15}\n"

            return table

        except Exception as e:
            self.logger.error(f"Error formatting pricing table: {e}")
            raise