# To print all elements of the list.
list=[1,2,3,4,578,65,43,2,23]
for i in list:
    print(i,end=" ")
print("\n")
# To print all elements of a tuple.
Fruits=("Apple","Mango","Orange","Banana","Pineapple")
for i in Fruits:
    print(i,end=" ")
else:
    print("End")

# To search for a number X in the tuple using for loop.
tup=(1,4,9,16,25,36,49,64,81,100)
a=0
print("Tuple : ",tup)
X=int(input("Enter the number to find: "))
for i in tup:
    if(i==X):
        print(X,"is found in the tuple at",a+1,"th location.")
        break  
    a+=1
else:   
    print(X,"is not found in the tuple.")

# Range fucntion()
# To print all even numbers from 0 to 10
for i in range(2,11,2):
    print(i)

# Pass Statement.
for i in range(0,10,3):
    pass
print("Code after pass.")