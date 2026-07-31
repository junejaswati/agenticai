#!/usr/bin/env python
import sys
import warnings
import os
from dotenv import load_dotenv

from datetime import datetime

from stock_picker.crew import StockPicker

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

load_dotenv()

SERPER_API_KEY = os.getenv("SERPER_API_KEY")
PUSHOVER_TOKEN = os.getenv("PUSHOVER_TOKEN")
PUSHOVER_USER_KEY = os.getenv("PUSHOVER_USER_KEY")

def run():
    """
    Run the crew.
    """
    inputs = {
        'sector': 'Technology',
        'current_date': str(datetime.now().date())
    }

    try:
        StockPicker().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")




    