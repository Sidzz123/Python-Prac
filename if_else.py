# Program to print what the color of light indicates 
light=input("Enter the color of light: ")
if(light == "Red"):
    print("Stop")
elif(light == "Yellow"):
    print("Ready")
elif(light == "Green"):
    print("Go")
else:
    print("Light is Broken")

# Program to print grades according to the student.
marks = int(input("Enter the marks scored by student: "))
if(marks<40):
   print("Grade : D")
elif(marks>=40 and marks<60):
   print("Garde : C")
elif(marks>=60 and marks<80):
   print("Grade : B")
elif(marks>=80 and marks<=100):
   print("Grade : A")
else:
   print("Marks must be out of 100")
   