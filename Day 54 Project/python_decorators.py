## Python Decorator Functions with Arguments
import time

def delay_decorator(function):
    def wrapper_function(*args, **kwargs):
        time.sleep(2)
        function(*args, **kwargs)
    return wrapper_function

@delay_decorator
def say_hello():   
    print("Hello")
    

def say_bye():
    print("Bye")

def set_greeting():
    print("How are you?")

decorated_function = delay_decorator(set_greeting)
delay_decorator()