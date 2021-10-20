# lets suppose we declare no from 1-10 in  a list
ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
c_e = 0
s_e = 0
for i in ls:
    if(i % 2 == 0):
        c_e += 1
        s_e += i
print(c_e, "\n", s_e)
