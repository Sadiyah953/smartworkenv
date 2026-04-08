import sys
import os

# Ensure Hugging Face /app is in path
sys.path.insert(0, "/app")

from env import SmartWorkEnv

if __name__ == "__main__":
    env = SmartWorkEnv()
    print("Environment started")
