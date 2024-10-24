# WAP to check if a number entered by the user is odd or even.
a=int(input("Enter the number: "))
if(a%2==0):
    print("The number entered is even.")
else:
    print("The number entered is odd.")

# WAP to find the greatest of 3 numbers entered by the user.
n1=int(input("First number: "))
n2=int(input("Second number: "))
n3=int(input("Third number: "))

if(n1>n2):
    if(n1>n3):
        print(n1,"is the greatest number.")
elif(n2>n3):
    print(n2,"is the greatest number.")
else:
    print(n3,"is the greatest number.")

# WAP to check if a number is a multiple of 7 or not.
b=int(input("Enter the number to check: "))
if(b%7==0):
    print(b,"is a multiple of 7.")
else:
    print(b,"is not a multiple of 7.")    