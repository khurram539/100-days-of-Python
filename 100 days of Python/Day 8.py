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
    
greet_with("Nowhere", "Khurram")

# Function arguments 

greet_with(name="Khurram", location="Virginia")

# Calculate the length of paint needed to paint the wall
# 1 can of paint can cover 5 square meters of wall 
# Given a random height and width of wall, calculate how many cans of paint you'll need to buy

import math 
def paint_calc(height, width, cover):
    area = height * width
    num_cans = math.ceil(area / cover)
    print(f"You'll need {num_cans} cans of paint.")
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
covrage = 5
paint_calc(height=test_h, width=test_w, cover=covrage)

# Prime Number Checker

def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")





    
