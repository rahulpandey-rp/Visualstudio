def cube(side_len):
    if(side_len > 0):
        return(side_len*side_len*side_len)
    else:
        return("Please Enter correct value")


side = int(input("Please enter the length of cube"))
print(cube(side))
