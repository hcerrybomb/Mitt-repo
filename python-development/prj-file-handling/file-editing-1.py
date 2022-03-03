OpenFile = open("C:\\Users\\wista002\\Desktop\\test_file.txt", "r")
#WriteFile = open("C:\\Users\\wista002\\Desktop\\test_file.txt", "w")

content = OpenFile.read()

print(content)


WriteFile = open("C:\\Users\\wista002\\Desktop\\test_file.txt", "w")

WriteFile.write(content)
WriteFile.write("\nMORE NUMBERSSS")

content = OpenFile.read()

print(content)
OpenFile.close()

