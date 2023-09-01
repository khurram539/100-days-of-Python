# Day 6 - Functions, code blocks and while loops

print("Hello World")

len("Hello")
num_char = len("Hello")  # len() is a function
print(num_char)

def my_function():
    print("Hello")
    print("Bye")
my_function()

def my_function_with_args(username, greeting):
    print("Hello, %s , From My Function!, I wish you %s" % (username, greeting))
my_function_with_args("khurram", "a great year!")



# Indentation is important in Python

def my_function():
    print("Hello")
    
def my_function():
    if sky == "clear":
        return "blue"
    elif sky == "cloudy":
        return "grey"
    print("Hello")  # This line will not be executed
print("Word") # This line will be executed

# Escaping the maze game

def turn_right():
    turn_left()
    turn_left()
    turn_left()
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()





