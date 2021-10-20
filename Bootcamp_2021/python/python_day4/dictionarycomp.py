dictionary = {'language': 'python', 'version': '3.8', 'app': None, 'ide': None}
new_dictionary = {
    key: value for key, value in dictionary.items() if value is not None
                    }
print(new_dictionary)
