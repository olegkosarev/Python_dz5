

my_dict = dict(One='Один', Two ='Два', Three  ='Три', Four  ='Четыре')

my_file =  open(r"C:\Users\1\Desktop\GB\python\lesson-5\for_task_4.txt", "r")

my_list = [line.split(" - ") for line in my_file]

new_list = [my_dict.get(el[0]) + " - " + el[1] for el in my_list]

out_file = open(r"C:\Users\1\Desktop\GB\python\lesson-5\out_file_task_4.txt", "w")

out_file.writelines(new_list)
out_file.close()