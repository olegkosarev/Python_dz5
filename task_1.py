out_f = open(r"C:\Users\1\Desktop\GB\python\lesson-5\out_file.txt", "w")

str_list = []

while True:
	stroka = input("Введите строку ")
	if stroka == "":
		break

	str_list.append(stroka+"\n")


out_f.writelines(str_list)
out_f.close()