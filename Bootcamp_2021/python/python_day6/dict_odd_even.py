def odd_even(list_nat_num):
    dict_odd_even = dict()
    try:
        for i in list_nat_num:
            if(type(i) != int):
                raise TypeError
            if(i == 0):
                raise ValueError
    except TypeError:
        print("Please enter literals with base 10")
    except ValueError:
        print("Please provide a list with Natural numbers only")
    else:
        dict_odd_even["Even"] = list(
                                filter(
                                    lambda x: x % 2 == 0, list_nat_num
                                    )
                                    )
        dict_odd_even["Odd"] = list(filter(lambda x: x % 2 != 0, list_nat_num))
        print(dict_odd_even)


odd_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
odd_even([0, 1, 2, 3, 4, 5, 6, 7, 8.2])
