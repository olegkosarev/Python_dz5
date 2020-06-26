
from statistics import mean 

my_file =  open(r"C:\Users\1\Desktop\GB\python\lesson-5\staff.txt", "r")

my_list = [line.split() for line in my_file]

print("Сотрудники с зп меньше 20 тыс: "+', '.join([el[0] for el in my_list if int(el[1])<20000]))

print("Средняя зп: "+str(mean(int(el[1]) for el in my_list)))
