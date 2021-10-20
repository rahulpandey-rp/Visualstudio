def floor1(num):
    if(num < 0):
        return(float(int(num)-1))
    else:
        return(float(int(num)))


def ceil1(num):
    if(num < 0):
        return(float(int(num)))
    else:
        return(float(int(num)+1))


n = float(
    input(
        "Please input a number \n "
        )
        )
print(floor1(n))
print(ceil1(n))
