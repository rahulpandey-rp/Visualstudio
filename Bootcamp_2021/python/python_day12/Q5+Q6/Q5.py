def replace_text(filepath, search_term, new_term, replace_all = False):
    with open(filepath,"r+") as file:
        text = file.read()
        if(replace_all):
            new_text = text.replace(search_term, new_term)
        elif( not replace_all):
            new_text = text.replace(search_term, new_term,1)
        file.seek(0)
        file.write(new_text)


replace_text("/home/rahul/Visualstudio/python/python_day12/Q5+Q6/file.txt", "Rahul", "Alice", True)