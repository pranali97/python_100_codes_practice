"""Types of Arguments"""
# POSITION
# KEYWORD
# DEFAULT
# VARIABLE LENGTH 


def add(a,b):    #Formal arguments
    c = a+b
    print(c)


add(2,3)   #Actual Arguments  -->   # POSITION
                                    # KEYWORD
                                    # DEFAULT
                                    # VARIABLE LENGTH 



def person(name,age=18):
    print(name)
    print(age)
# person(25,"pranali")                # POSITION
# person(age=25,name ="pranali")        # KEYWORD
person("pranali",30)

# ----------------------------------------------------------------------------------------------------------------------------
print("--------------------------------------------------------------------------------------------------------------------")

def sum(a,*b):
    # c = a + b
    # print(a)
    # print(b)
    c = a
    for i in b:     #VARIABLE LENGTH  
        c = c + i 
    print(c)

sum(10,20,30,40,50)  