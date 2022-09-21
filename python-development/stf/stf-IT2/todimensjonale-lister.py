from pandas import DataFrame



#! OPPGAVE 1
list1 = []
for i in range(5):
    list1.append([0,0,0,0,0])
print(DataFrame(list1),'\n\n')



#! OPPGAVE 2
list2 = []
for i in range(5):
    
    if i == 0 or i == 4:
        list2.append([1,1,1,1,1])
    else: 
        list2.append([0,0,0,0,0])

print(DataFrame(list2),'\n\n')



#! OPPGAVE 3
list3 = []
for i in range(5):
    list3.append([1,0,0,0,1])
print(DataFrame(list3),'\n\n')



#! OPPGAVE 4
list4 = []
for i in range(8):
    proxlist = []
    for j in range(8):
        count = i + j
        col = "H" if count%2==0 else "S"
        proxlist.append(col)
    list4.append(proxlist)
print(DataFrame(list4),'\n\n')