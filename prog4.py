def anagram_func(str1,str2):
    if sorted(str1)==sorted(str2):
        return True
    else:
        return False

str1 = input("Enter a string: ")
str2 = input("Enter a string: ")

if anagram_func(str1,str2):
    print(sorted(str1))
    print(sorted(str2))
    print("Anagram")
else:
    print(sorted(str1))
    print(sorted(str2))
    print("Not Anagram")





# a = 'qwerty'
# c = sorted(a)
# print(sorted(a))