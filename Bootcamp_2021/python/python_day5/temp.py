def convert_cel_to_far(cel_temp):
    return(cel_temp * 9 / 5 + 32)


def convert_far_to_cel(far_temp):
    return((far_temp - 32) * 5 / 9)


f_temp = float(input("Enter the temperatue in Fahrenheit"))
print(f"{f_temp} degrees F = {convert_far_to_cel(f_temp):.2f} degrees C")
c_temp = float(input("Enter the temperature in celsius"))
print(f"{c_temp} degrees C = {convert_cel_to_far(c_temp):.2f} degrees F")
