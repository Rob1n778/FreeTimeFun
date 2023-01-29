import random
import time
import os

# Prompt the user to enter values for the start, end, step, and limit of a range of random numbers
start = int(input("Enter start-value: ") or (1))
end = int(input("Enter end-value: ") or (1000))
step = int(input("Enter step-value: ") or (1))
limit = int(input("How many numbers? ") or (100))

# Create a list of random numbers within the specified range and step, limited by the user's input
list = [random.randrange(start, end + 1, step) for i in range(limit)]

# Write the list to a text file at a specific file path, and also print out to the console
with open('list.txt', 'w') as f:
    f.write(" ".join(str(x) for x in list))
    print("\nDone!\n")

# Check if the user wants to open the file in Notepad
open_notepad = input("Open notepad to see result? (y/n) ")
if open_notepad == "y" or open_notepad == "Y":
    file_path = "list.txt"
    os.startfile(file_path)