def decorator(fn):
    def text_count(*args):
        with open("/home/rahul/Visualstudio/python/python_day12/Q5+Q6/file.txt","r") as file:
            data = file.read()
            print(f"The cound of word to be replaced is {data.count(args[1])}")
            
        fn(*args)

    return text_count


@decorator
def replace_text(filepath, search_term, new_term, replace_all = False):
    with open(filepath,"r+") as file:
        text = file.read()
        if(replace_all):
            new_text = text.replace(search_term, new_term)
        elif( not replace_all):
            new_text = text.replace(search_term, new_term,1)
        file.seek(0)
        file.write(new_text)


replace_text("/home/rahul/Visualstudio/python/python_day12/Q5+Q6/file.txt", "Alice", "Rahul", True)