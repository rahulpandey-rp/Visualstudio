num_list = [2, 3, 4, 5, 6]
iter_obj = iter(num_list)
while True:
    try:
        print(next(iter_obj)*2)
    except StopIteration:
        break
