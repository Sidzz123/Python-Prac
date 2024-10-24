# WAP to print number from n to 1 backwards using recursion.
def printn(n):
    if(n==0):
        return 
    print(n,end=" , ")
    printn(n-1)

# WAF to print the elements of a list using recursion.
def lisele(list,i=0):
    if(i==len(list)):
        return
    print(list[i],end=" , ")
    lisele(list,i+1)

num=int(input("Please enter a number: "))
printn(num)
print("\n")

eledevice=["T.V.","Fridge","Computer","Smartphone","Washing Machine",37,901.3,39393.33,56,"Electric press"]
lisele(eledevice)
