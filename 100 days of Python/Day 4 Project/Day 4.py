# Day 4 - random module and Python lists

import random
random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() 
print(random_float)

random_float * 5
print(random_float)

# Random module

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

# List

state1 = "California"
state2 = "Oregon"
states_of_america = ["California", "Oregon", "Washington", "Texas"]
print(states_of_america[0])

# List methods - Who will pay the bill

import random 
# split string method
names_string = input("Give me everybody's names, separated by a comma. ") # input names
names = names_string.split(", ") # split names into a list

# get the total number of items in list
num_items = len(names)
# generate random numbers between 0 and the last index
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + " is going to buy the meal today!")

# treasure map

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print = (f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
horizontal = int(position[0]) #2
vertical = int(position[1])  #3
selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"







