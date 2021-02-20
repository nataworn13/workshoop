import json

json_string = '{ "name": "fuji and nut", "age":21, "city":"Chonburi"}'

python_dict = json.loads(json_string)

print(python_dict["name"])
print(python_dict["age"])
print(python_dict["city"])