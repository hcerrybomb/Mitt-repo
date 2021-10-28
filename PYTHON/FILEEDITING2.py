def CreateFileAndAdd():
    YesOrNo = str(input("would you like to create a file?: " ))
    if YesOrNo == "yes":
        FirstLines = str(input("what will the first lines be: "))
        open("C:\\Users\\wista002\\Desktop\\test.txt", "w").write(FirstLines)
    if YesOrNo == "no":
        print("ok, exiting program.")

def SearchSomethingInFile():
    OpenFile = open("C:\\Users\\wista002\\Desktop\\test.txt", "r")
    FileContent = OpenFile.read()
    String = FileContent
    String = str(String)
    String = String.lower()
    FileContentList = String.split("\n")
    Search = str(input("Search here: "))    
    for n in range(len(FileContentList)):
        if Search in FileContentList[0+n]:
            print("success, search is in line: ", n)
            SuccessCount = 1
    if SuccessCount != 1:
        print("not found in this file")
    OpenFile.close()
            
def AddStringToFile():
    
    NewContentInput = str(input("The new stuff: "))
    print("\n\n")
    NewContent = '\n'+NewContentInput    
    OpenFile = open("C:\\Users\\wista002\\Desktop\\test.txt", "r")    
    PreviousContent = OpenFile.read()
    print('\x1b[0;30;42m' + "Previous file content:" + '\x1b[0m' + '\n')
    print(PreviousContent)
    print("\n\n")    
    import time
    time.sleep(3)        
    print('\x1b[0;30;42m' + "New file content:" + '\x1b[0m')
    print(NewContent)
    print("\n\n")    
    CurrentContent = PreviousContent + NewContent
    CurrentContent = str(CurrentContent)    
    open("C:\\Users\\wista002\\Desktop\\test.txt", "w").write(CurrentContent)
    print('\x1b[0;30;42m' + "Current file content" + '\x1b[0m' + '\n')
    print(CurrentContent)
    print("\n\n")
    OpenFile.close()

print("have you created a database?")
CreatedOrNot = str(input("yes/no: "))
if CreatedOrNot == "no":
    CreateFileAndAdd()
if CreatedOrNot == "yes":
    
    print("would you like to search or add to the database?")
    SeacrhOrAdd = str(input("search/add: "))
    if SeacrhOrAdd == "add":
        AddStringToFile()
    if SeacrhOrAdd == "search":
        SearchSomethingInFile()



    

    




