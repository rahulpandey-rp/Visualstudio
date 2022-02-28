from datetime import datetime
from functools import wraps
def logger(filepath):
    def decorator(fn):
        @wraps(fn)
        def wrappers(*args,**kwargs):
            result=fn(*args)
            with open(filepath,"w") as file:
                write_list=[]
                write_list.append(f"Log_of_function: {fn.__name__}\n")
                write_list.append(
                    f"Timestamp: {str(datetime.now().strftime('%d-%m-%Y %I:%M:%S %p'))}\n")
                result = fn(*args)
                write_list.extend(
                    [f"Input_parameters: {args}\n",
                    f"Result: {result}\n"]
                )
                file.writelines(write_list
                    )

        return(wrappers)
    return(decorator)



@logger("/home/rahul/Visualstudio/python/python_day12/Q7/file.log") 
def sum(a, b):
	return (a + b)
sum(2,4)
