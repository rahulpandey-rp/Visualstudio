def oldAge(d):
    if("age" in d.keys()):
        age = d['age']
        age += 50
    else:
        age = 50
    print(age)


oldAge({"name": "Aayush", "age": 24})  # prints 74
oldAge({"name": "Aayush"})             # prints 50
