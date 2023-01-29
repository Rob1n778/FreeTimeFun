import random
import os

# Function to find the minimum number in the list and its position
def min_num(the_list):
    min_num = min(the_list)
    print("Minimum value is:", min_num)
    print("Minimum value is at position:", the_list.index(min_num))

# Function to find the maximum number in the list and its position
def max_num(the_list):
    max_num = max(the_list)
    print("Maximum value is:", max_num)
    print("Maximum value is at position:", the_list.index(max_num))

# Function to count the number of elements in the list
def count_num(the_list):
    print("The list has", len(the_list), "numbers in it.")

# Function to find the sum of all elements in the list
def sum_num(the_list):
    print("The sum of all numbers in list is:", sum(the_list))

# Function to sort the list in ascending order
def sort_asc(the_list):
    the_list.sort()
    print("The list has been sorted in ascending order.")

# Function to sort the list in descending order
def sort_desc(the_list):
    the_list.sort(reverse=True)
    print("The list has been sorted in descending order.")

# Function to shuffle the elements in the list
def shuffle_num(the_list):
    random.shuffle(the_list)
    print("The list has been shuffled.")

# Function to convert the list to exponential notation
def exp_num(the_list):
    the_list = ["{:e}".format(x) for x in the_list]
    print("The list has been converted to exponential notation.")

# Dictionary containing all the functions as values and their names as keys
actions = {"min": min_num, "max": max_num, "count": count_num, "sum": sum_num,
           "sort asc": sort_asc, "sort dec": sort_desc, "shuffle": shuffle_num, "exp": exp_num}

file_path = "C:/Dev/FreeTimeFun/January_2023/Applications/random_generator/dist/list.txt"

# Check if the file "list.txt" exists
if os.path.exists(file_path):
    with open(file_path, "r") as f:
        # Read the list from the file and convert each element to an int
        the_list = [int(x) for x in f.read().split()]
    while True:
        # Ask the user for the action they want to perform on the list
        action = input("min, max, count, sum, sort asc, sort dec, shuffle, exp (Enter to exit) ")
        # Check if the input is a valid key in the actions dictionary
        if action in actions:
            actions[action](the_list)
            # Ask the user if they want to open the file to see the result
            open_file = input("Open file to see result? (y/n) ")
            if open_file == "y" or open_file == "Y":
                os.startfile(file_path)
        elif action == "":
            break
        else:
            print("Invalid input!")