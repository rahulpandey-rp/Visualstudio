def division(numerat, denominat):
    try:
        if(type(numerat) != int and type(denominat) == int):
            raise TypeError
        if(numerat < 0 or denominat < 0):
            raise ValueError
        result = round(numerat / denominat, 2)
    except TypeError:
        print("Literal found with base other than int")
    except ValueError:
        print("Please provide whole numbers as Value")
    except ZeroDivisionError:
        print("Please do not divide by zero")
    else:
        print(result)


division(2, 3)
division(2, 0)
division(2, 3.8)
division("a", 5)
division(5, "a")
division(6, -5)
