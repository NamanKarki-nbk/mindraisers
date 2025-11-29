
# A decorator is a function that wraps another function to add new functionality without changing the original function’s code.

#count execution time
# import time

# def timer(func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         print(f"Execution time: {end-start} sec")
#         return result
#     return wrapper

# @timer
# def slow_function():
#     time.sleep(1)
    
# slow_function()


#decorator with parameters