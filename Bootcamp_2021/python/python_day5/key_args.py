def kwargs_demo(**kwargs):
    print(len(kwargs))
    print(*kwargs.keys())
    print(*kwargs.values())


product_with_types = {
                "Apple": "fruit", "Orange": "fruit",
                "Book1": "stationary", "book2": "stationary",
                "book3": "stationary", "guava": "fruit"
                    }
kwargs_demo(**product_with_types)
