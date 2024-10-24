Age=int(input("Enter your Age."))
if (Age>= 18):
    print("Voter Eligible to vote .")
    print("Proceed Forward.")
else:
    print("Not eligible ")
    
for i in range(2):
    for Age in range(30):
        print(Age,end="")
