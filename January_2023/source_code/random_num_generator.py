import random
import time

start = int(input("Enter start-value: ") or (1))
end = int(input("Enter end-value: ") or (1000))
step = int(input("Enter step-value: ") or (1))
limit = int(input("How many numbers? ") or (100))

list = [random.randrange(start, end + 1, step) for i in range(limit)]

with open('list.txt', 'w') as f:
    f.write(" ".join(str(x) for x in list))
    for i in list:
        print(f"{i}", end=" ")
    print("\nDone!")
time.sleep(5)