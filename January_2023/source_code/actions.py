import random
import os

with open("list.txt", "r") as f:
    the_list = list(map(int, f.read().split()))

while True:
    action = input("min, max, count, sum, sort asc, sort dec, shuffle, exp (Enter to exit) ")
    if action != 'min' and action != 'max' and action != 'count' and action != 'sum' and action != 'sort asc' and action != 'sort dec' and action != "exp" and action != "shuffle":
        if action == "":
            break
        print("Invalid input!\n")
        continue
    elif action == "min":
        min_num = min(the_list)
        print("Minimum value is:", min_num)
        print(f"Minimum value is at position:", the_list.index(min_num))
    elif action == "max":
        max_num = max(the_list)
        print("Maximum value is:", max_num)
        print(f"Maximum value is at position:", the_list.index(max_num))
    elif action == "count":
        print(f"The list has {len(the_list)} numbers in it.")
    elif action == "sum":
        print(f"The sum of all numbers in list is: {sum(the_list)}")
    elif action == "sort asc":
        sorted_asc = sorted(the_list)
        with open("list.txt", "w") as fp:
            fp.write(" ".join(str(x) for x in sorted_asc))
        print("The list has been sorted in ascending order.")
        open_notepad = input("Open notepad to see result? (y/n) ")
        if open_notepad == "y" or open_notepad == "Y":
            file_path = "list.txt"
            os.startfile(file_path)
        else:
            continue
    elif action == "sort dec":
        sorted_dec = sorted(the_list, reverse=True)
        with open("list.txt", "w") as fp:
            fp.write(" ".join(str(x) for x in sorted_dec))
        print("The list has been sorted in decending order.")
        open_notepad = input("Open notepad to see result? (y/n) ")
        if open_notepad == "y" or open_notepad == "Y":
            file_path = "list.txt"
            os.startfile(file_path)
        else:
            continue
    elif action == "shuffle":
        random.shuffle(the_list)
        with open("list.txt", "w") as fp:
            fp.write(" ".join(str(x) for x in the_list))
        print("The list has been shuffled.")
        open_notepad = input("Open notepad to see result? (y/n) ")
        if open_notepad == "y" or open_notepad == "Y":
            file_path = "list.txt"
            os.startfile(file_path)
        else:
            continue
    elif action == "exp":
        exp_number = []
        for i in the_list:
            int_number = i
            exp_number.append("{:e}".format(int_number))
        with open("list.txt", "w") as fp:
            fp.write(" ".join(str(x) for x in exp_number))
    else:
        print("Something's went wrong!")