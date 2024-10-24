# WAP to ask the user to enter names of their 3 fav movies and store them in a list.
list_movie=[]

m1=input("Enter your 1st favourite movie: ")
m2=input("Enter your 2nd favourite movie: ")
m3=input("Enter your 3rd favourite movie: ")

list_movie.append(m1)
list_movie.append(m2)
list_movie.append(m3)

print(list_movie)

# WAP to check if a list contains a palindrome of elements.
l1=[1,2,4,5,4,2,1]
# Do the following three lines or simply use reverse method of list.
l2=[]
for i in range(0,7):
    l2.insert(i,l1[6-i]) 
if(l2==l1):
    print("The list is palindrome. ")
else:
    print("The list is not palindrome. ")