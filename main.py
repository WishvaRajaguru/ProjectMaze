import os.path
from PIL import Image, ImageDraw
from Scripts.agent import Agent

print("Hi there, what is the maze you want me to solve today!")
file = str(input("eg maze.txt: "))
if os.path.exists(file):
    print("I can apply 2 algorithms to this maze. Should I use the default? (y/n) \n\t 1.Stack Approach (Default) \n\t 2.Queue Approach")
    alg = input("")

    if alg == "y" or "n":
        agent = Agent(file, alg)
        agent.start_process()
    else:
        print("Invalid algorithm applied!")
else:
    print(f"The file {file} does not exists!")
