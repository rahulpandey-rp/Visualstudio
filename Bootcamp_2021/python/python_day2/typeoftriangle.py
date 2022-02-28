s1, s2, s3 = map(
                int,
                input(
                    "Please Enter the Sides of triangle by giving a space"
                    ).split()
                )
if(s1 == s2 and s2 == s3):
    print("Equilateral Triangle")
elif(s1 != s2 and s2 != s3 and s3 != s1):
    print("Scalene Triangle")
elif(s1 == s2 or s2 == s3 or s3 == s1):
    print("Isoceles Triangle")
