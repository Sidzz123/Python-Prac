# WAF to print the length of the list.
def lislenprint(list):
    print(len(list))

# WAF to print the elements of a list in a single line.
def printlist(list):
    for i in list:
        print(i,end=", ")

# WAF to find the factorial of a number n.(n is the parameter)
def factorialfind(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact

    
# WAF to convert USD to INR.
def curconv(usd):
    inr=usd*84.045
    return inr

# WAF to print even for even number and odd for odd number.
def eveod(n):
    if(n%2==0):
        return("EVEN")
    else:
        return("ODD")

fruits=["Apple","orange","madarine","kiwi","pineapple","mango","lichi"]
cities=['delhi','mumbai','gurgaon']
lislenprint(cities)
lislenprint(fruits)

print("List 1 - ",end="")
printlist(cities)
print()
print("List 2 - ",end="")
printlist(fruits)
print()

Num=int(input("Enter the number to find factorial: "))
print("Factorial of",Num,"is :",factorialfind(Num))

Dollars=int(input("enter how many dollars to be converted : "))
print(Dollars,"$ is",curconv(Dollars),"Rs in india.")

n1=int(input("Enter the number to check if even or odd: "))
print(eveod(n1)) 