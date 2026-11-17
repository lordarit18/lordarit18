info = {
    "key":"value",
    "name":"John Doe",
    "learning":"Python",
    "age": 30,
    "is_adult":"True",
}


print(info)
print(type(info))

print(info["name"])
print(info["learning"])

info["name"] = "Arit Mondal"
print(info)

null_dic = {}
null_dic["name"] = "Arit Mondal"
null_dic["age"] = 30
print(null_dic)

students = {
    "name" : "Arit mondal",
    "phy": 90,
    "chem": 80, 
}
print(students)

print(len(students.keys()))
print(list(students.keys()))