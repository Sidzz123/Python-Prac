# WAP to count the number of students with "A" grade in the tuple.

T1=("C","D","A","A","B","B","A")
print("Number of students with grade A: ",T1.count("A"))

# Store the above values in a list and sort them from "A" to "D".
L=[]
for i in range(0,len(T1)):
    L.insert(i,T1[i])
L.sort()
print("Sorted list from the tuple: ",L)