#%%
import matplotlib.pyplot as plt
OpenFile = open("C:\\Users\\wista002\\Desktop\\babymasser.txt", "r")
FileContent = OpenFile.read()
String = FileContent
String = str(String)
FileContentList = String.split("\n")
#vettafaen hva "avvik" er 
for i in range(0, len(FileContentList)):
    FileContentList[i] = int(FileContentList[i])
print("antall babyer=", len(FileContentList),"\nmax er=", max(FileContentList), "\nmin er=", min(FileContentList), "\ngjennomsnitt=", sum(FileContentList) / len(FileContentList))
plt.hist(FileContentList, bins=100)
# %%
