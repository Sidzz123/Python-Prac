#String Definition using Single ,Double and Triple Qoutes.
str1="String with Double quotes."
str2='String with single quotes.'
str3='''String with triple quotes. '''
print('',str1,"\n",str2,'\n',str3)

# String Concatenation
str=str1+str3
print(str)

#String length operation.
str4="This is a string"
a=len(str4)
print(a)

#Indexing in String.
str5="This is me Siddharth singh Bhandari."
ch=str5[12]  #Accessing characters of sting using index .
print(ch)

#String Slicing.
str6="This is the sixth String of this program."
print(str6[1:7])
print(str6[ :6])
print(str6[3: ])
print(str6[8:len(str6)])

#Negative Indexing 
string="Myself Shubham"
print(string[-4])
print(string[-8:-2])
print(string[-5: ])

#String Functions
str7="he is a coder and a student."
print(str7)
print(str7.endswith("ey."))
str7=str7.capitalize()
print(str7)
str7=str7.replace("and","or")
print(str7)
print(str7.find("coder"))
print(str7.count("a"))