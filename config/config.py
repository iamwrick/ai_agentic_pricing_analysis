"""
Configuration management module.
Handles loading and validating environment variables and configuration settings.
"""

import os
from dotenv import load_dotenv
from pathlib import Path
from typing import Dict
import yaml
from dataclasses import dataclass


@dataclass
class APIConfig:
    """API configuration settings."""
    openai_api_key: str
    tavily_api_key: str


@dataclass
class AppConfig:
    """Application configuration settings."""
    debug_mode: bool
    log_level: str
    output_directory: str


class ConfigManager:
    """Manages application configuration and environment variables."""

    def __init__(self, config_path: str = None):
        """
        Initialize configuration manager.

        Args:
            config_path (str, optional): Path to YAML config file
        """
        # Load environment variables
        load_dotenv()

        # Load YAML config if provided
        self.config_data = self._load_yaml_config(config_path) if config_path else {}

        # Validate required environment variables
        self._validate_env_variables()

        # Set up configurations
        self.api_config = self._setup_api_config()
        self.app_config = self._setup_app_config()

    def _load_yaml_config(self, config_path: str) -> Dict:
        """Load YAML configuration file."""
        try:
            with open(config_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            print(f"Error loading config file: {e}")
            return {}

    def _validate_env_variables(self):
        """Validate required environment variables."""
        required_vars = ['OPENAI_API_KEY', 'TAVILY_API_KEY']
        missing_vars = [var for var in required_vars if not os.getenv(var)]

        if missing_vars:
            raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")

    def _setup_api_config(self) -> APIConfig:
        """Set up API configuration."""
        return APIConfig(
            openai_api_key=os.getenv('OPENAI_API_KEY'),
            tavily_api_key=os.getenv('TAVILY_API_KEY')
        )

    def _setup_app_config(self) -> AppConfig:
        """Set up application configuration."""
        return AppConfig(
            debug_mode=self.config_data.get('debug_mode', False),
            log_level=self.config_data.get('log_level', 'INFO'),
            output_directory=self.config_data.get('output_directory', 'reports')
        )

    def initialize_apis(self):
        """Initialize API configurations."""
        os.environ['OPENAI_API_KEY'] = self.api_config.openai_api_key
        os.environ['TAVILY_API_KEY'] = self.api_config.tavily_api_key