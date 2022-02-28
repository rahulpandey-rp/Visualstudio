d = int(input("Give the number to calculate the sum\n"))
n = 10
sum = 0
while(d != 0):
    sum += d % n
    d = d // n
print(sum)
