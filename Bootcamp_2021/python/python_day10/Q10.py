num_list = [77, 88, 44, 33]
map_list = list(map(lambda x: x % 10, num_list))
comp_list = [num % 10 for num in num_list]
print(map_list)
print(comp_list)
