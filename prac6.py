# WAP to store following word meaning in a python dictionary.

D1={"Table":("A piece of furniture","list of facts and figures"),
    "Cat":"A small animal"}
print(D1)   

# You are given a list of subjects for students. Assume one classroom required for 1 subject.
# How many classrooms are nedded by all students? 

Student_Subject={"python","java","c++","python","javascript","java","python","java","c++","C"}
print("Classrooms required by students :",len(Student_Subject))

# WAP to enter marks of three subjects from the user and store them in dictionary. Start with an empty dictionary 
# and add one by one. Use subject name as key and marks as value.

D2={}
m1=int(input("Enter marks for english : "))
m2=int(input("Enter marks for Python : "))
m3=int(input("Enter marks for Cpp : "))

D2.update({"English":m1,"Python":m2,"Cpp":m3})
print(D2)

# Figure out a way to store 9 and 9.0 as diffrent elements in a set. Can take help of built-in data type .

S1={9,(9.0,)}
print(S1)