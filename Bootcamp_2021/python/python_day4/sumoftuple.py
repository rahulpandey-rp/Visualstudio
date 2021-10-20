list = [(0, 1), (1, 2), (2, 3)]
sum_value = 0
for tup in list:
    sum_value += tup[1]
print(sum_value)
print(sum([item[1] for item in list]))
