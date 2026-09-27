from time import time, ctime
from functools import wraps
import os

def log(filename=None):
    def wrapper(func):
        @wraps(func)
        def inner(*args, **kwargs):
            start_time = time()
            try:
                result = func(*args, **kwargs)
                end_time = time()
            except Exception as e:
                log_info = f"Time: {ctime(start_time)}. Function {func.__name__} error: {e}. Inputs: {args}, {kwargs}"
                if filename is None:
                    print(log_info)
                else:
                    log_file_path = os.path.join("..", f"{filename}.txt")
                    with open(log_file_path, "a", encoding="utf-8") as file:
                        file.write(log_info + "\n")
                raise Exception(e)
            else:
                log_info = (f"Time: {ctime(start_time)}. "
                            f"Function {func.__name__} is OK. "
                            f"Inputs: {args}, {kwargs}. Elapsed time: {end_time - start_time:.2f} sec. "
                            f"Result: {result}")
                if filename is None:
                    print(log_info)
                else:
                    log_file_path = os.path.join("..", f"{filename}.txt")
                    with open(log_file_path, "a", encoding="utf-8") as file:
                        file.write(log_info + "\n")
            return result

        return inner

    return wrapper


@log(filename="log")
def foo(a, b):
    return a / b

print(foo(2, 3))
