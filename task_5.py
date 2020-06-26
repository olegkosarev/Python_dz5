import random
from itertools import count

path = r"C:\Users\1\Desktop\GB\python\lesson-5\out_file_task_5.txt"

out_file = open(path, "w")

numbers = []

for el in count(1):
    if el > 15:
        break
    else:
        numbers.append(str(random.randint(1,10000)))

out_file.write(' '.join(numbers))
out_file.close()

my_file =  open(path, "r")

read_numbers = [el for el in my_file][0].split(" ")

print(sum(int(el) for el in read_numbers))

#print(sum(read_numbers))


