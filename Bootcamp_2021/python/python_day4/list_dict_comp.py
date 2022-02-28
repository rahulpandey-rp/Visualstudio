tup_list = [(0, 1), (1, 2), (2, 3)]
dictionary = {key: sum(list(key)) for key in tup_list}
print(dictionary)
print(dictionary[(2, 3)])
