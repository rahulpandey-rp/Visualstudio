with open("/home/rahul/Visualstudio/python/python_day12/Q1/heya.txt","r") as file:
    data = file.read()
    print(data)

with open("/home/rahul/Visualstudio/python/python_day12/Q1/heya.txt","w") as file:
    file.write("Shutup\n")
    file.write("You are not supposed to be here\n")

with open("/home/rahul/Visualstudio/python/python_day12/Q1/heya.txt","r") as file:
    data = file.read()
    print(data)

with open("/home/rahul/Visualstudio/python/python_day12/Q1/heya.txt","a") as file:
    file.write("Shutup this is new line by append\n")
    file.write("You are not supposed to be here This is append use\n")

with open("/home/rahul/Visualstudio/python/python_day12/Q1/heya.txt","r") as file:
    data = file.read()
    print(data)