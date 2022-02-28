product_with_types = {
    "Apple": "fruit",
    "Orange": "fruit",
    "Book1": "stationary",
    "book2": "stationary",
    "book3": "stationary",
    "guava": "fruit"
    }
list_of_fruits = []
for key in product_with_types:
    if(product_with_types[key] == "fruit"):
        list_of_fruits += [key]
print(list_of_fruits)
