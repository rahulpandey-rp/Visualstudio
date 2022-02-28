num_list = [2, 3, 4, 5, 6, 7, 8, 9]
increment_list = list(map(lambda x: x + (x * .05), num_list))
print(increment_list)
