import sys


sys.setrecursionlimit(2000)
# print(sys.getrecursionlimit())
i = 0
def greet():
    global i                     # global i  UnboundLocalError: local variable 'i' referenced before assignment
    i+=1
    print("Good day",i)
    greet()

greet()
