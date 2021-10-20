def sum_of_digit(num):
    digit_sum = 0
    while(num != 0):
        digit_sum += num % 10
        num = num // 10
    return(digit_sum)

if __name__ == "__main__":
    sum_of_digit(123)