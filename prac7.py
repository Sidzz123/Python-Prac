# WAP to find  the sum of first n numbers. (using while)
n=int(input("Enter the value of n: "))
i=1
sum=0
while(i<=n):
    sum=sum+i
    i+=1
print("Sum of first",n,"numbers is: ",sum)

# WAP to find factorial of first n numbers. (using for)
n1=int(input("Enter number to find factorial: "))
fact=1
for i in range(1,n1+1):
    fact=fact*i
print("Factorial of",n1,"is :",fact)