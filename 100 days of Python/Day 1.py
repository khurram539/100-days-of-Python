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

#fix the code below

print("Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# input () will get user input in console
# Then print() will print the word "Hello" and the user input

print("Hello " + input("what is your name?"))

input ("What is your name? ")
print(len("Khurram"))

name = "khurram"
print(name)

name = "Angelina"
print(name)

# Dont change the code below
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a: " + a)
print("b: " + b)

# Create a greeting for your program.
print("Welcome to the Band Name Generator.")
# Ask the user for the city that they grew up in.
city = print("What's name of the city you grew up in?\n")
# ask the user for the name of a pet.
print("What's your pet's name?\n")
# Combine the name of their city and pet and show them their band name.
print("Your band name could be " + city + " " + pet)
# Make sure the input cursor shows on a new line, see the example at:
print("https://band-name-generator-end.appbrewery.repl.run/")