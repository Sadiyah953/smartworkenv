import sys
import os

sys.path.insert(0, "/app")

from env import SmartWorkEnv

if __name__ == "__main__":
    env = SmartWorkEnv()
    print("Environment started")
