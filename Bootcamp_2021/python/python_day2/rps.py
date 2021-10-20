c = int(input("Please enter the number of Dataset"))
dp = input("Enter the data pairs")
for i in range(0, c*2, 2):
    if dp[i] == dp[i+1]:
        print("Draw")
    elif dp[i] == "R":
        if dp[i + 1] == "P":
            print("B wins")
        elif dp[i + 1] == "S":
            print("A wins")
    elif dp[i] == "P":
        if dp[i + 1] == "S":
            print("B wins")
        elif dp[i + 1] == "R":
            print("A wins")
    elif dp[i] == "S":
        if dp[i + 1] == "R":
            print("B wins")
        elif dp[i + 1] == "P":
            print("A wins")
