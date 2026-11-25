student = {
    "name": "Gowtham",
    "age": 28,
    "city": "Vizag"
}
#print the dictionary
print(student)


#print the value of a specific key
print(student["name"])


#add a new key-value pair to the dictionary
student["phone"] = 1234567890

print(student["phone"])

#chabge the value of an existing key in the dictionary
student["age"] = 30

print(student)


#remove a key-value pair from the dictionary
student.pop("age")

print(student)


#get the number of key-value pairs in the dictionary
print(len(student))


#get the keys of the dictionary
print(student.keys())


#get the values of the dictionary
print(student.values())     

#get the key-value pairs of the dictionary
print(student.items())

