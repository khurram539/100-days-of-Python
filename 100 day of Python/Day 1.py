# Working with variables in python to manage data
# quiz 1: skill Assesment

print(len("95637+12"))

score = 67
if score < 80 and score > 70:
    print("A")
elif score < 90 and score > 80:
    print("B")
elif score > 60:
    print("C")
else:
    print("D")
    


def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
result = outer_function(5, 10)
print(result)

def foo(a, b=4, c=5):
    print(a, b, c)
    
foo(20, c=12)

def all_aboard(a, *args, **kw):
    print(a, args, kw)
all_aboard(4, 7, 3, 0, x=10, y=64)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num + 3 for num in numbers if num % 2 == 0]
print(result)

# Printing the console in python

print("Hello World")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("This is my first python program")
print("Hello" + " Khurram")

