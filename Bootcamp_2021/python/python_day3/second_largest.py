num_list = [23, 12, 431, 1324, 23, 12]
first_max, second_max = 0, 0
for num in num_list:
    if(first_max < num):
        second_max = first_max
        first_max = num
    elif(second_max < num):
        second_max = num
print(first_max, second_max)
