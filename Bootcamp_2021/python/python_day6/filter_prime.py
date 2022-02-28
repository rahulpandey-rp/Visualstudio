num_list = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17]
prime_list = list(
                filter(
                    lambda x:
                    all(x % i != 0 for i in range(2, x)) is True,
                    num_list
                    )
                )
print(prime_list)
