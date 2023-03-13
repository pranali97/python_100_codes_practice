# def is_even(n):
#     return n%2==0

# n = [3,5,6,7,1,8,12,9,23]

# evens = list(filter(is_even, n))
# print(type(evens))
# print(evens)




j = [2,4,3,5,6,10]
evens = list(filter((lambda i:i%2==0),j))

def update(n):
    return n*2

# doubles = list(map(update,evens))  #map function
doubles = list(map(lambda n : n*2,evens))

def add_all(a,b):
    return a+b

from functools import reduce

# sum = reduce(add_all,doubles)
sum = reduce(lambda a,b:a+b,doubles)


# print(evens)
# print(doubles)
print(sum)