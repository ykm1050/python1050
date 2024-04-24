import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

radius = 5
circle_area = calculate_circle_area(radius)
print("The area of the circle with radius", radius, "is:", circle_area)



import os

def list_files_and_directories(path="."):
    print("Files and directories in", os.path.abspath(path) + ":")
    for entry in os.listdir(path):
        print(entry)

list_files_and_directories()



import sys

def print_arguments():
    
    arguments = sys.argv
    print("Script name:", arguments[0])

    if len(arguments) > 1:
        print("Arguments:")
        for arg in arguments[1:]:
            print(arg)
    else:
        print("No arguments provided.")

print_arguments()



import random

def roll_die():
    
    result = random.randint(1, 6)
    return result
print("Rolling the die 5 times:")
for i in range(5):
    print("Roll", i+1, ":", roll_die())



import datetime

def print_current_datetime():
    
    current_datetime = datetime.datetime.now()

    print("Current date and time:", current_datetime)

print_current_datetime()

