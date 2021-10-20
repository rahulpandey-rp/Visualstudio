sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, \
            sed do eiusmod tempor incididunt ut labore et dolore magna \
            aliqua.Ut enim ad minim veniam, quis nostrud exercitation \
            ullamco laboris nisi ut aliquip ex ea commodo consequat. \
            Duis aute irure dolor in reprehenderit in voluptate velit \
            esse cillum dolore eu fugiat nulla pariatur. Excepteur \
            sint occaecat cupidatat non proident, sunt in \
            culpa qui officia deserunt mollit anim id est laborum."
frequency_char = dict()
maximum_occuring_char = "L"
for char in sentence:
    if(char.isalpha() or char.isnumeric()):
        if(char in frequency_char):
            frequency_char[char] += 1
        else:
            frequency_char[char] = 0
        if(frequency_char[maximum_occuring_char] < frequency_char[char]):
            maximum_occuring_char = char
print(frequency_char)
print(f"maximum occuring char is {maximum_occuring_char} \
    with frequency {frequency_char[maximum_occuring_char]}")
