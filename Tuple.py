tup=(1,4,2,"Real","Unreal",1)
print(tup)
print(tup[4])
# tup[2]=337  Tuple does not support item assignment.
# print(tup)
tup1=() # We can define empty tuple.
print(tup1)
tup2=(59,) # We can define tuple with single element using ',' else it is considered as just a variable.
print(tup2)
print(type(tup2))
# Tuple Slicing.
print(tup[1:4])
print(tup[2: ])
print(tup[ :3])

# Tuple Methods
# 1.Index - Used to find location of elemnt in tuple.
print(tup.index(4))

# 2.Count - Used to find Frequency of element in tuple.
print(tup.count(1))