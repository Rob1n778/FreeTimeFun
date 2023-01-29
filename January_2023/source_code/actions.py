import random
import os

file_path = "C:/Dev/FreeTimeFun/January_2023/Applications/random_generator/dist/list.txt"

while True:
    # Open the file "list.txt" and read the contents
    # into the variable "the_list" as a list of integers
    with open(file_path, "r") as f:
        the_list = list(map(int, f.read().split()))
    
    # Prompt the user for an action to perform on the list
    action = input("min, max, count, sum, sort asc, sort dec, shuffle, exp (Enter to exit) ")
    
    # Check if the input is valid
    if action != 'min' and action != 'max' and action != 'count' and action != 'sum' and action != 'sort asc' and action != 'sort dec' and action != "exp" and action != "shuffle":
        if action == "":
            break
        print("Invalid input!\n")
        continue
        
    # If the input is "min", find the minimum value and its index in the list and print them
    elif action == "min":
        min_num = min(the_list)
        print("Minimum value is:", min_num)
        print(f"Minimum value is at position:", the_list.index(min_num))
        
    # If the input is "max", find the maximum value and its index in the list and print them
    elif action == "max":
        max_num = max(the_list)
        print("Maximum value is:", max_num)
        print(f"Maximum value is at position:", the_list.index(max_num))
        
    # If the input is "count", print the length of the list
    elif action == "count":
        print(f"The list has {len(the_list)} numbers in it.")
        
    # If the input is "sum", print the sum of all numbers in the list
    elif action == "sum":
        print(f"The sum of all numbers in list is: {sum(the_list)}")
        
    # If the input is "sort asc", sort the list in ascending order and save it to the file
    # then prompt user if they want to see the result in notepad
    elif action == "sort asc":
        sorted_asc = sorted(the_list)
        # Write the sorted list to the specified file 
        with open(file_path, "w") as fp:
            fp.write(" ".join(str(x) for x in sorted_asc))
        print("The list has been sorted in ascending order.")
        # Check if the user wants to open the file in Notepad
        open_notepad = input("Open notepad to see result? (y/n) ")
        if open_notepad == "y" or open_notepad == "Y":
            os.startfile(file_path)
        else:
            continue
            
    # If the input is "sort dec", sort the list in descending order and save it to the file
    # then prompt user if they want to see the result in notepad
    elif action == "sort dec":
        sorted_dec = sorted(the_list, reverse=True)
        # Write the sorted list to the specified file
        with open(file_path, "w") as fp:
            fp.write(" ".join(str(x) for x in sorted_dec))
        print("The list has been sorted in descending order.")
        # Check if the user wants to open the file in Notepad
        open_notepad = input("Open notepad to see result? (y/n) ")
        if open_notepad == "y" or open_notepad == "Y":
            os.startfile(file_path)
        else:
            continue
    # Shuffle the list
    elif action == "shuffle":
        random.shuffle(the_list)
        # Write the shuffled list to the specified file
        with open("list.txt", "w") as fp:
            fp.write(" ".join(str(x) for x in the_list))
        print("The list has been shuffled.")
        # Check if the user wants to open the file in Notepad
        open_notepad = input("Open notepad to see result? (y/n) ")
        if open_notepad == "y" or open_notepad == "Y":
            os.startfile(file_path)
        else:
            continue
    # Convert the list elements to exponential notation
    elif action == "exp":
        exp_number = []
        for i in the_list:
            int_number = i
            exp_number.append("{:e}".format(int_number))
        # Write the list in exponential notation to the specified file
        with open("list.txt", "w") as fp:
            fp.write(" ".join(str(x) for x in exp_number))
    else:
        print("Something went wrong!")