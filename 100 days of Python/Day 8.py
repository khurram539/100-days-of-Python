# Day 8 - Function Parameters & Caesarer Cipher


def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

greet()

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Khurram")

# Positional Arguments VS Keyword Arguments

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")
    
greet_with("Khurram", "Miami")