import json

courses = '{ "name":"John", "age":[30, 45], "car":null }'

data = json.loads(courses)
print(type(data))
print(data["name"])
print(data["age"][1])
