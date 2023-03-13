class computer:
    def __init__(self):
        self.name =  "pranali"
        self.age = 25


c1 = computer()  #object c1 is in heap memory 
c2 = computer()  #object c2 is in heap memory

c1.name = "rashi"
c1.age = 32
print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)

print(id(c1))
print(id(c2))