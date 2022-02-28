import time
million_num_list_1 = []
start = time.time()
for num in range(0, 1000000):
    million_num_list_1.append(num)
end = time.time()
print(f"time taken by using for loop {end - start}")
start = time.time()
million_num_list_2 = [num for num in range(0, 1000000)]
end = time.time()
print(f"time taken by using list comprehension {end - start}")
