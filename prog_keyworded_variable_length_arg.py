def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)

person("pranali",age = 25,fav_colour="BLack",chocolate="Silk")  #if u want to pass multiple data and that too with keyword then with the help of variable length keyword argument