def convert_cel_to_far(cel_temp):
    return(cel_temp * 9 / 5 + 32)


def convert_far_to_cel(far_temp):
    return((far_temp - 32) * 5 / 9)


if "__main__"==__name__:
    convert_cel_to_far(6)
    convert_far_to_cel(6)
