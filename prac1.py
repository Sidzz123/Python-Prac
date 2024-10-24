# Program for if-elif-else prac.
A= int (input("A: "))
G= input("M/F: ")

if((A==1 or A==2) and G=="M"):
    print("Fee is 100")
elif(A==3 or A==4 or G=="F"):
    print("Fee is 200")
elif(A==5 and G=="M"):
    print("Fee is 300")
else:
    print("No Fee")
a="3.14"
print(type(a))
a=float(a) # Type Casting 
print(type(a))
print(a+2) # Type Conversion