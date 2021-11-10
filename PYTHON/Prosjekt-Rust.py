import subprocess
#runthing = subprocess.run(["EXE PATH OF RUST"])
from time import time, ctime, sleep
t = time()
b = str(ctime(t))
c= b.split(" ")
print(c)
print(c[3])
d= c[3].split(":")
print(d)
print(d[0],d[1])
e = d[0] + d[1]
print(e)
while e != "1451":

    print("not time yet")
    sleep(1)

else:
    print("time")

