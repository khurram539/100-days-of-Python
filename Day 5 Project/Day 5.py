# Day 5 - For Loops, Ranges, and Code Blocks

# for loops

fruit = ["Apple", "Peach", "Pear"]
for fruit in fruit:
    print(fruit)
    print(fruit + " Pie")
    
# for loops with range
for number in range(1, 11, 3):
    print(number)
    
# Average height 

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(total_height)

number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(number_of_students)

# High Score

student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")

# Adding Evens numbers

total = 0
for number in range(2, 101, 2):
    total += number
print(total)
for number in range(1, 101):
    if number % 2 == 0:
        total += number
print(total)

# FizzBuzz

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)

# Password Generator

import random
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Cap_letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]
print ("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Eazy Level 

password_list = []

for car in range(1, nr_letters + 1):
    password_list += random.choice(letters)
    
for car in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

for car in range(1, nr_numbers + 1):
    password_list += random.choice(number)
for car in range(1, nr_numbers + 1):
    password_list += random.choice(Cap_letters) 

  
print(password_list)
random.shuffle(password_list)
print(password_list)

password = ""
for car in password_list:
    password += car
print(f"Your password is: {password}")



  


