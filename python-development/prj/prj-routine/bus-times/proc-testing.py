from multiprocessing import Process
import time
import sys

def func1():
    i = 0
    while i < 20:
        i += 1
        time.sleep(1)
        print(i)

def func2():
    x = 0
    while x < 20:
        x += 1
        time.sleep(1)
        print(x)
def func3():
    x = 0
    while x < 20:
        x += 1
        time.sleep(1)
        print(x)
def func4():
    x = 0
    while x < 20:
        x += 1
        time.sleep(1)
        print(x)
def func5():
    x = 0
    while x < 20:
        x += 1
        time.sleep(1)
        print(x)
def func6():
    x = 0
    while x < 20:
        x += 1
        time.sleep(1)
        print(x)
def func7():
    x = 0
    while x < 20:
        x += 1
        time.sleep(1)
        print(x)
if __name__=='__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p3 = Process(target=func3)
    p3.start()
    p4 = Process(target=func4)
    p4.start()
    p5 = Process(target=func5)
    p5.start()
    p6 = Process(target=func6)
    p6.start()
    p7 = Process(target=func7)
    p7.start()


