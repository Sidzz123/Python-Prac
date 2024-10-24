# Set is a collection of unordered and unique objets.
S1={1,2,3,5,6,4}
print(S1)
print(type(S1))

# Duplicacy prohibeted in sets.
s2={44,7,44,8,"he","she","hey","he",2,3,4,6} # Multiple duplicacy of elements .
print(s2) #Each element read and stored only once.
print(type(s2))

# Empty set
s3=set()
print(type(s3))
print(s3)

# Set Methods
# 1.Add()
s3.add("New")
s3.add(5)
s3.add(4)
s3.add(3)
s3.add("element")
print(s3)

# 2.Remove()
s3.remove("element")
print(s3)

# 3.clear()
s3.clear()
print(s3)

# 4.pop()
s4={3,5,6,7,9,45,23,100,33,24,1}
print(s4.pop())
print(s4) 

# 5.union()
# print(S1.union(s2))
s5=S1.union(s2)
print(s5)

# 6.intersection()
# print(S1.intersection(s2))
s6=S1.intersection(s2)
print(s6)