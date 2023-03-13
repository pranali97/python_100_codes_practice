# write a program to swap a numbers 

# method 1

a = int(input("Enter a 1st number. "))
b = int(input("Enter a 2nd number. "))

temp = a
a = b
b = temp

print("After swapping value of a is: ", a)
print("After swapping value of b is: ", b)

# method 2

a = int(input("Enter a 1st number. "))
b = int(input("Enter a 2nd number. "))

a, b =b, a

print("After swapping value of a is: ", a)
print("After swapping value of b is: ", b)

# mathematical operator 


a = int(input("Enter a 1st number. "))
b = int(input("Enter a 2nd number. "))

a = a+b  #10 + 20
b = a-b  
a = a-b

print("After swapping value of a is: ", a)
print("After swapping value of b is: ", b)

