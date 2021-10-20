x = 79
if(x < 10):
    # using f-string
    print(f"The number x whose value is {x} is less than 10")
    # using string.format
    print("The number x whose value is {} is less than 10".format(x))
else:
    # using f-string
    print(f"The number x whose value is {x} is greater than 10")
    # using string.format
    print("The number x whose value is {} is greater than 10".format(x))
