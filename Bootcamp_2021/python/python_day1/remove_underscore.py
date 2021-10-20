st1 = "hello_how_are__you"
len_st1 = len(st1)
st2 = ""
for i in range(len_st1):
    if(st1[i] == "_"):
        st2 += "+"
    else:
        st2 += st1[i]
print(st1)
print(st2)
print(st1.replace("_", "+"))
