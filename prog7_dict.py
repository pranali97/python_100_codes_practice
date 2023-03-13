list_1 = ['Black','Blue','Orange']
list_2 = ['Berry','Rays','Colour']

combined1 = dict(zip(list_1,list_2))
combined2 = list(zip(list_1,list_2))
combined3 = tuple(zip(list_1,list_2))
combined4 = set(zip(list_1,list_2))
print(combined1)
res = combined1['Black']
combined1['Red'] = 'Rose'
combined1['white'] = 'Jamun'
del combined1['Red']
print("deleted",combined1)
# res = combined1['Red']
print(res)
print(combined2)
print(combined3)
print(combined4)