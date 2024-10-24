# Program to store marks of 5 students in a list.
marks=[35,64.34,79,68,22]
print(marks)  # Display the list elements without accessing each element.
print(type(marks)) # Data type list.
print(marks[4]) # Can access elements individually.
print(len(marks)) # To get the length of list.
marks[0]=291 # Mutable data type, can change elements. 
print(marks) 
print(marks[2:4]) # List slicing.

# List Methods.
# 1.Append
marks.append(483838.292)
print(marks)

# 2.Sort
marks.sort()
print(marks)
marks.sort(reverse=True)
print(marks)

# 3.Reverse
marks.reverse()
print(marks)

# 4.Insert 
marks.insert(1,64.34)
print(marks)

# 5.Remove
marks.remove(64.34)
print(marks)

# 6.Pop
marks.pop(2)
print(marks)