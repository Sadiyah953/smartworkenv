import sys
import os

# Ensure /app is in Python path inside Hugging Face Space
sys.path.insert(0, "/app")

from tasks.email_task import process_email
from tasks.data_cleaning_task import clean_data
from tasks.scheduling_task import schedule_meeting

class SmartWorkEnv:
    def __init__(self):
        pass

    def step(self, action):
        processed = process_email("Hello")
        cleaned = clean_data([1, 2, 3])
        schedule_meeting("10:00 AM")
        return processed, cleaned

    def reset(self):
        pass

    def state(self):
        return {}
