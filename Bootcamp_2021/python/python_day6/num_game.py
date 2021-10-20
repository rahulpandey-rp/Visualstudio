while True:
    try:
        num = int(input("Please Enter a Number"))
    except ValueError as Vp:
        print("Please enter a literal with base 10")
        print(Vp)
        print("Try Again")
    else:
        print(f"You entered a number {num} Wohooo!")
        break
