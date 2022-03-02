

OpenFile = open("C:\\Users\\wista002\\Desktop\\test.txt", "r")
FileContent = OpenFile.read()
FileContentList = FileContent.split("\n")
print(FileContentList)
Search = str(input("Search here: "))
for n in range(len(FileContentList)):
    if Search in FileContentList[0+n]:
        print("success")