import json
student = {
    "name": "Gowtham",
    "age": 22,
    "city": "Hyderabad",
    "course": "Python",
    "marks": 90
}

print(student)


"""Write JSON to a file"""
# Write JSON data to the file with indentation for readability
with open("student.json", "w") as file:
    json.dump(student, file, indent=4) 


"""Read JSON from a file"""
# Read JSON data from the file
with open("student.json", "r") as file:
    data = json.load(file)

print(data)
print(data["name"])
print(data["marks"])

"""Convert Python object to JSON string"""

student = {"name": "Gowtham", "age": 22}
"""Function	ఉపయోగం
json.dump()	JSON fileలో write
json.dumps()	JSON stringగా convert
json.load()	JSON file నుంచి read
json.loads()	JSON string నుంచి Python data"""
result = json.dumps(student)

print(result)
print(type(result))


"""Convert JSON string to Python object"""
data = '{"name": "Gowtham", "age": 22}'

result = json.loads(data)

print(result["name"])
print(type(result))


#Data Update inside JSON file
with open("student.json", "r") as file:
    data = json.load(file)

data["marks"] = 95

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

print("Marks Updated Successfully")