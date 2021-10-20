import random
again = "y"
while(again != "n"):
    u_n = int(input("Please Enter a number between 1 to 50\n"))
    r_n = random.randint(1, 50)
    if(r_n == u_n):
        print("YOu guessed Right, Hurray!")
        guess = True
    elif(r_n > u_n):
        print("Ah, The number you entered is a Smaller than the right number")
        guess = False
    else:
        print("Ah, The number you entered is a greater than the right number")
        guess = False
    if(not guess):
        again = input("Do you want to play again y/n")
