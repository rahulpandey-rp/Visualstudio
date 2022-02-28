try:
    string = input("Please Enter a String: ")
    Index = int(input("Please Input the index Number: "))
    if(len(string) <= Index):
        raise IndexError
except ValueError as VAlueE:
    print("Please enter an integer with base 10")
    print(VAlueE)
except IndexError:
    print(
        f"Index out of bound Please Check if index is less \
        than length of string: {len(string)}")
else:
    print(string[Index])
