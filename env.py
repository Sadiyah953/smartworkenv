import sys
import os

sys.path.insert(0, "/app")

from tasks.email_task import process_email
from tasks.data_cleaning_task import clean_data
from tasks.scheduling_task import schedule_task

from graders.email_grader import grade_email
from graders.data_grader import grade_data
from graders.schedule_grader import grade_schedule


class SmartWorkEnv:

    def step(self, task_type, data):
        if task_type == "email":
            result = process_email(data)
            score = grade_email(result)

        elif task_type == "data":
            result = clean_data(data)
            score = grade_data(result)

        elif task_type == "schedule":
            result = schedule_task(data)
            score = grade_schedule(result)

        else:
            result = "Invalid task"
            score = 0.0

        return {"result": result, "score": score}

    def reset(self):
        return "Environment reset"

    def state(self):
        return "Running"
