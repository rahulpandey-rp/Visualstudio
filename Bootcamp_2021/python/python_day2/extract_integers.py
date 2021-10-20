# lets declare tuple with data as name of fruits and pricew of fruits.
tuple_mixed_data = ("Banana", "Guava", 20, 98, 34, "Apple", 73, 33, "Pears")
extracted_integers = []
for data in tuple_mixed_data:
    if(type(data) == int):
        extracted_integers += [data]
print(extracted_integers)
