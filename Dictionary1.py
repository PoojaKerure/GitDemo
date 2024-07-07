# friends={'tom':'111-222-333',
#          'jerry':'666-33-111'}
# print(friends)
#
# #Retriving elements ...
#
# print(friends['tom'])
#
# #adding element.....
# friends['bob']='888-999-666'
# print(friends)
#
# #modify value...
# friends['bob']='888-999-777'
# print(friends)
#
# #delete dictionary.....
# del friends['bob']
# print(friends)

#Looping items in the dictionary,....

# Values={'a':'100',
#          'b':'200',
#          'c':'300',
#          'd':'400'}

# for x in Values:
#     print(x,":",Values[x])

#length of dictionary....
# values={'a':'100',
#         'b':'200',
#         'c':'300',
#         'd':'400'}
# print(len(values))


#Equality tests in dictionary...
# d1={'mike':41,'bob':3}
# d2={'bob':3,'mike':41}
#
# print(d1==d2)
# print(d1!=d2)

# friends={'tom':'111-222-333','bob':'888-999-666','jerry':'666-333-111'}
#
# print(friends.popitem())
#
# print(friends)
# print(friends.clear())

friends={'tom':'111-222-333','bob':'888-999-666','jerry':'666-333-111'}

# print(friends.keys())
# print(friends.values())
# print(friends.get('jerry'))
print(friends)
print(friends.pop('tom'))
print(friends)
























