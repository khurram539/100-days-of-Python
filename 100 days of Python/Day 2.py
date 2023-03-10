# Day 2

# Data types

# String

("Hello"[4])

print("123" + "345")

123_456_789

# float

3.14159

# Dont changge the code below
two_digit_number = input("Type a two digit number: ")
# Don't change the code above

####################################
#Write your code below this line
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

print(first_digit)
print(second_digit)

result = first_digit + second_digit
print(result




score = 0
height = 1.8
iswinning = True
# f-String
print(f"your score is {score}, your height is {height}, you are winning is {iswinning}")


age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(months_remaining)
message =f"you have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left."
print(message)

# How to build a tip calculator

#if the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tips_as_percent = tip / 100
total_tip_amount = bill * tips_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_acount = print(bill_per_person, 2)
print(f"Each person should pay: ${final_acount}")
