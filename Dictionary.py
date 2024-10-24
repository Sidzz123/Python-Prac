# Defining a Dicionary.
Dicti={"Name": "Tarun",
      "CGPA": 9.67,
      "Marks":[78,89,76,90],}
print(Dicti)

# Tuples as key for a dictionary
Info={("str1",34,67.89):["life",8383,90.21],
      ("list_str1",768,940.56,True):132.55,}
print(Info) 

# Dictionary inside Dictionary
Nest_Dic={1:"Value1",
          (2,4,3,"Key2"):{"Nested_dict_key1":"Nest_Dict_value1", 2:"value2",},
          45:"value3"}
print(Nest_Dic)

# Accessing value of a dictionary inside another Dictionary.
print(Nest_Dic[(2,4,3,"Key2")][2])

# Accessing values of dictionaries with thier keys.
print(Dicti["Name"],Info[("str1",34,67.89)],Nest_Dic[1])

# Replace values with new values for a key.
Dicti["Marks"]=[91,99,94,89,98]
print(Dicti)
 
# Dictionary Methods
# 1. Dict.keys()
a=Dicti.keys()
print(a) 
print(list(a)) # Printing all keys of the dictionary in list type.

# 2. Dict.Values()
print(Nest_Dic.values())
print(tuple(Nest_Dic.values())) # Type casting values in tuple.

# 3. Dict.item()
print(Dicti.items())    

# 4. Info.get()
print(Info.get(("str1",34,67.89)))

# 5. Nest_Dic.update()
Nest_Dic.update({4:"4th value"})
print(Nest_Dic)