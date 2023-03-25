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

def paint_calc(height, width, cover):
    area = height * width
    cans = area / cover
    print(f"You'll need {cans} cans of paint.")

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
