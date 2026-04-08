import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from env import SmartWorkEnv

env = SmartWorkEnv()

# Example runs
print(env.step("email", {"email": "Hello"}))
print(env.step("data", {"numbers": [1, None, 2, 3]}))
print(env.step("schedule", {"event": "Meeting", "time": "10 AM"}))
