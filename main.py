"""
Main entry point for the AI pricing analysis application.
"""

from pathlib import Path
from src.analysis.pricing_analyzer import PricingAnalyzer
from src.utils.logger import setup_logger
from config.config import ConfigManager

logger = setup_logger(__name__)

def main():
    """Main function to run the AI pricing analysis."""
    try:
        # Initialize configuration
        config_path = Path('config/config.yaml')
        config_manager = ConfigManager(str(config_path) if config_path.exists() else None)

        # Initialize APIs
        config_manager.initialize_apis()

        logger.info("Starting AI Model Pricing Analysis...")
        analyzer = PricingAnalyzer()
        report = analyzer.run_analysis()

        print("\nAnalysis Report")
        print("==============")
        print(report)

    except Exception as e:
        logger.error(f"Application error: {e}")
        raise

if __name__ == "__main__":
    main()