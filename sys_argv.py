# ch = eval(input("Enter a character: "))
# print(ch)

# x = 5
# y = 6

# z = x+ y
# print(z)

import sys   #Command line arguments are those values that are passed during calling of program along with the calling statement.
x = int(sys.argv[1])  #python3 sys_argv.py 8 9
print(type(x))
y = int(sys.argv[2])
z = x * y
print(z)


