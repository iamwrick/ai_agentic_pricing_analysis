"""
Setup configuration for ai_agentic_pricing_analysis package.
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

# Read requirements from requirements.txt
def read_requirements(filename: str):
    return [line.strip() for line in (this_directory / filename).read_text().splitlines()
            if line.strip() and not line.startswith('#')]

setup(
    name="ai_agentic_pricing_analysis",
    version="0.1.0",
    author="Your Name",
    author_email="wrick.talukdar@gmail.com",
    description="An agentic system for AI model pricing analysis using CrewAI",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/ai_agentic_pricing_analysis",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements("requirements.txt"),
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "isort>=5.0",
            "mypy>=0.900",
            "flake8>=4.0",
            "pre-commit>=2.17",
        ],
        "docs": [
            "sphinx>=4.0",
            "sphinx-rtd-theme>=1.0",
            "myst-parser>=0.18",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-pricing-analysis=ai_agentic_pricing_analysis.main:main",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/iamwrick/ai_agentic_pricing_analysis/issues",
        "Source": "https://github.com/iamwrick/ai_agentic_pricing_analysis",
        "Documentation": "https://ai-agentic-pricing-analysis.readthedocs.io/",
    },
    include_package_data=True,
    package_data={
        "ai_agentic_pricing_analysis": [
            "config/*.yaml",
            "data/*.json",
        ],
    },
)