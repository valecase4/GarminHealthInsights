# Garmin Health Insights

## Garmin Health Insights: A Data-Driven Exploration of Heart Rate and Activity Trends

Garmin Data Analysis Project: Exploring heart rate and activity trends using data collected from the GarminConnect API. Includes data cleaning, analysis, and reporting phases.

## Tools

- __Python__ 🐍: Core language for data collection, cleaning, and analysis.
- __VS Code__ 💻: Code editor for development and debugging.
- __Jupyter Notebook__ 📒: Interactive environment for data exploration and visualization.
- __Git__ 🌱: Version control to track changes and collaborate effectively.

### API Connection Test

The script ``test/api.py`` serves as a first step to ensure successful communication with the GarminConnect API. It verifies the following:

1. __Authentication__
2. __Basic API Call__: Fetches a sample activity
3. __Error Handling__: Detects and reports potential issues

### Initial Architecture of the Project

``data/``: This folder contains all project data. <br>
- ``data/raw``: Stores raw data collected directly from the API
- ``data/cleaned``: Stores processed and cleaned data ready for the analysis. <br>
``script.py``: This script handles the interaction with the GarminConnect API. It fetches raw data such as heart rate, steps, and sleep data for further processing. <br>
``main.ipynb``: A Jupyter Notebook for performing statistical analysis, visualizing trends, and generating insights using the cleaned data.<br>
``.env``: A file for securely storing sensitive information, such as API credentials (email and password). This file is excluded from version control for security purposes.