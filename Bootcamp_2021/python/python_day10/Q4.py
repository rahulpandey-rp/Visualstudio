def double(num_list):
    for num in num_list:
        yield(num*2)


num_list = [2, 3, 4, 5, 6]
counter = double(num_list)
while True:
    try:
        print(next(counter))
    except StopIteration:
        break
