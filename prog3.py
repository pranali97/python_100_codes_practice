def count_char(string,char):
    count = 0
    for i in range(len(string)): #1 to 6
        if string[i]==char:
            count=count +1
    return count

string = input("Enter a string: ")  #quesol 
char =  input("enter a character: ")  # e
count = count_char(string,char)
print("Total no. of occurance is char ",char,"is: ",count)