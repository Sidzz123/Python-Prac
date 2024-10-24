# Fucntion to find sum of two numbers.
def sum(n1,n2):
    S=n1+n2
    return S

# Fucntion to find average of 3 numbers.
def avg(a,b,c):
    avera=(a+b+c)/3
    return avera


a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
print("Sum of first two numbers is : ",sum(a,b))
c=int(input("Enter third number : "))
print("Average of all three numbers is : ",avg(a,b,c))