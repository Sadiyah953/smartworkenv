import sys
import os

# Force Python to see tasks folder in Hugging Face Docker
sys.path.insert(0, "/app/tasks")
sys.path.insert(0, "/app/graders")

from email_task import process_email
from data_cleaning_task import clean_data
from scheduling_task import schedule_meeting

class SmartWorkEnv:
    def __init__(self):
        pass

    def step(self, action):
        # Example
        processed = process_email("Hello")
        cleaned = clean_data([1, 2, 3])
        schedule_meeting("10:00 AM")
        return processed, cleaned

    def reset(self):
        pass

    def state(self):
        return {}
