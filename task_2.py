
my_file =  open(r"C:\Users\1\Desktop\GB\python\lesson-5\out_file.txt", "r")


my_line = [line for line in my_file]

my_word = [str(len(line.split())) for line in my_line]

print("количество строк в файле: "+str(len(my_line)))

print("количество слов в строках: "+str(my_word))
