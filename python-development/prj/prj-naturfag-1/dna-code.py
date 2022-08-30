import random

start = 0

AntallBaser = int(input("Hvor mange baser?: "))
tid = AntallBaser
DNAlist = []
import time

while start < AntallBaser:
    HvilketDna = random.randint(1,4)
    if HvilketDna == 1:
        Dna = '\x1b[0;30;45m' + " A " + '\x1b[0m'
    if HvilketDna == 2:
        Dna = '\x1b[0;30;46m' + " T " + '\x1b[0m'
    if HvilketDna == 3:
        Dna = '\x1b[0;30;43m' + " C " + '\x1b[0m'
    if HvilketDna == 4:
        Dna = '\x1b[0;30;42m' + " G " + '\x1b[0m'
    DNAlist.append(Dna)
    start = start + 1

mRNAlist = []

for x in range(len(DNAlist)):
    if DNAlist[x] == '\x1b[0;30;45m' + " A " + '\x1b[0m':
        mRNA = '\x1b[0;30;45m' + " U " + '\x1b[0m'
    if DNAlist[x] == '\x1b[0;30;46m' + " T " + '\x1b[0m':
        mRNA = '\x1b[0;30;46m' + " A " + '\x1b[0m'
    if DNAlist[x] == '\x1b[0;30;43m' + " C " + '\x1b[0m':
        mRNA = '\x1b[0;30;43m' + " G " + '\x1b[0m'
    if DNAlist[x] == '\x1b[0;30;42m' + " G " + '\x1b[0m':
        mRNA = '\x1b[0;30;42m' + " C " + '\x1b[0m'
    mRNAlist.append(mRNA)

print(" ")
print("Estimert tid ", tid/10000 * 45 * 2 + 1,"sekunder")
time.sleep(1)
print(" ")
print("Starter program")
print(" ")

Var1 = 0

for x in range(len(DNAlist)):
    print(DNAlist[x],end='')
    time.sleep(0.002)
    Var1 = Var1 + 1
    if Var1 % 25 == 0:
        print("\n",end='')

def mRNAtråd(mRNAlist):
    print(' ')
    print("\nKomplimentær mRNA tråd: \n")
    time.sleep(1)
    
    Var2 = 0
    
    for x in range(len(mRNAlist)):
        print(mRNAlist[x],end='')
        time.sleep(0.002)
        Var2 = Var2 + 1
        if Var2 % 25 == 0:
            print("\n",end='')
    
KjørmRNA = str
def KJØRmRNAtråd(KjørmRNA):
    print(" ")
    KjørmRNA = str(input("Lage komplimentær mRNA tråd? (Ja/Yes eller Nei/No): "))
    if KjørmRNA == "ja":
        mRNAtråd(mRNAlist)
        print("\n\nProgram over")
    elif KjørmRNA == "Ja":
        mRNAtråd(mRNAlist)
        print("\n\nProgram over")
    elif KjørmRNA == "yes":
        mRNAtråd(mRNAlist)
        print("\n\nProgram over")
    elif KjørmRNA == "Yes":
        mRNAtråd(mRNAlist)
        print("\n\nProgram over")
    elif KjørmRNA == "nei":
        print("\nOk, Program over")
    elif KjørmRNA == "Nei":
        print("\nOk, Program over")
    elif KjørmRNA == "no":
        print("\nOk, Program over")
    elif KjørmRNA == "No":
        print("\nOk, Program over")
    else:
        print("\n\x1b[0;30;49mIkke gyldig svar\x1b[0m")
        KJØRmRNAtråd(KjørmRNA)
KJØRmRNAtråd(KjørmRNA)

    
