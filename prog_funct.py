# def greet():
#     print("Hi")
#     print("Hello")
# greet()


# def funct(x):

#     x = 8
#     print(x)

# funct(10)

# def add_sub(x,y):
#     r1 = x+y
#     r2 = x-y
#     return r1,r2

# result1, result2 = add_sub(6,8)
# print(result1, result2)


def update(x):
    print(id(x))
    x = 100
    print("x ", x, id(x))


a = 10
update(a)
print("a ", a, id(a))

# PASS BY VALUE 

# PASS BY REFERENCE 


def update(lst):
    print(id(lst))
    lst[1]= 25
    print(id(lst))
    print("lst",lst)


# print(id(lst))
lst = [10,20,30]
print(id(lst))
update(lst)
