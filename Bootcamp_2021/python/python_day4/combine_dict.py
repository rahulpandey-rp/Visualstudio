d1 = {'1': 1, '2': 2, '3': 3}
d2 = {'4': 4, '5': 5, '6': 6}
d3 = {}
d3.update(d1)
d3.update(d2)
print(f"using update method to combine dictionaries {d3}")
d4 = {**d1, **d2}
print(f"using kwargs to combine dictionaries {d4}")
d5 = d1 | d2
print(f"using Merge operator to combine dictionaries {d5}")
