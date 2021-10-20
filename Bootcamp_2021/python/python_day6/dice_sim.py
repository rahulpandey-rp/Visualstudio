import random
roll_list = list(map(lambda x: random.randint(1, 6), range(10000)))
print(sum(roll_list) / len(roll_list))
