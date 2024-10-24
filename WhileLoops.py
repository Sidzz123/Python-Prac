# To print the string 5 times.
str1="This is string"
i=0
while (i<5):
    print(str1)
    i+=1

# To print number from 1 to 100.
i=0
while(i<100):
    print(i+1)
    i+=1

# To print number from 100 to 1.
i=100
while(i>0):
    print(i)
    i-=1

# To print the multiplication table of a number n.
n=int(input("N : "))
i=1
while(i<=10):
    print(n,"*",i,"=",n*i)
    i+=1

# To print the elements of the list using  loop.
l=[1,4,9,16,25,36,49,64,81,100]
i=0
while(i<len(l)):
    print(l[i])
    i+=1

# To search for a number X using loop in the tuple.
T=(1,4,9,16,25,36,49,64,81,100)
i=0
flag=0
x=int(input("Number to find: "))
while(i<len(T)):
        if(T[i]==x):
            print(x,"found at index :",i)
            flag+=1
            break
        i+=1    
if(flag==0):
     print(x,"not found in tuple.")