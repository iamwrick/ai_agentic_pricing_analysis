"""
Logging configuration module.
Provides consistent logging setup across the application.
"""

import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Optional


def setup_logger(name: str, log_file: Optional[str] = None) -> logging.Logger:
    """
    Set up and configure logger with both console and file handlers.

    Args:
        name (str): Name of the logger (typically __name__)
        log_file (Optional[str]): Path to log file. If None, a default path will be used

    Returns:
        logging.Logger: Configured logger instance
    """
    # Create logs directory if it doesn't exist
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # If no log file specified, create one with timestamp
    if log_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = log_dir / f"ai_pricing_analysis_{timestamp}.log"

    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Create formatters and handlers
    console_formatter = logging.Formatter(
        '%(levelname)s - %(message)s'
    )

    file_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Console handler
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(console_formatter)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


def get_task_logger(task_name: str) -> logging.Logger:
    """
    Get a logger specifically for task tracking.

    Args:
        task_name (str): Name of the task

    Returns:
        logging.Logger: Logger configured for task tracking
    """
    logger = setup_logger(f"task.{task_name}")
    return logger


def log_execution_time(logger: logging.Logger):
    """
    Decorator to log function execution time.

    Args:
        logger (logging.Logger): Logger to use for timing logs
    """

    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = datetime.now()
            logger.debug(f"Starting execution of {func.__name__}")

            try:
                result = func(*args, **kwargs)
                execution_time = datetime.now() - start_time
                logger.debug(f"Completed {func.__name__} in {execution_time}")
                return result

            except Exception as e:
                logger.error(f"Error in {func.__name__}: {str(e)}")
                raise

        return wrapper

    return decorator