def perform_calculation(a, b):
    return((a + b, a - b))


res = perform_calculation(40, 10)
print(",".join(map(str, res)))
