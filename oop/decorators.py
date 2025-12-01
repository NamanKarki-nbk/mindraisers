
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


#staticmethod is a decorator that is used to define a method that does not operate on an instance of the class
#classmethod is a decorator that is used to define a method that operates on the class itself
#abstractmethod is a decorator that is used to define a method that must be implemented by any subclass


# import abc

# class Animal(abc.ABC):
#     @abc.abstractmethod
#     def sound(self):
#         pass    

# class Dog(Animal):
#     def sound(self):
#         print("Bark")

# dog = Dog()
# dog.sound()



from abc import ABC, abstractmethod

class teacher(ABC):

    @abstractmethod
    def teaches(self):
        pass


class MathTeacher(teacher):
    def teaches(self):
        print("Math Teacher")



obj1 = MathTeacher()
obj1.teaches()