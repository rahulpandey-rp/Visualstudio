num_list = [2, 3, 4, 5, 6]
generator = (num*2 for num in num_list)
for num in generator:
    print(num)
