# Day 30 - Errors , Exceptions, and JSON Data


try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")    


height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")


bmi = (weight / height ** 2)
print(bmi)


fruits= ["Apple", "Pear", "Orange"]


TODO Catch the exception and make sure the code runs without crashing.

def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("There is no fruit at that index.")
    else:
        print(f"A {fruit} pie.")


facebooks_posts = [
    {"Likes": 21, "Comments": 2},
    {"Likes": 13, "Comments": 2, "Shares": 1},
    {"Likes": 33, "Comments": 8, "Shares": 3},
    {"Comments": 4, "Shares": 2},
    {"Comments": 1, "Shares": 1},
    {"Likes": 19, "Comments": 3}
]
total_likes = 0
for post in facebooks_posts:
    try:
        total_likes = total_likes + post["Likes"]
    except KeyError:
        pass
print(total_likes)  
        
import pandas

data = pandas.read_csv("100-days-of-Python/Day 30 Project/nato_phonetic_alphabet.csv")

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    
    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        print(output_list)
generate_phonetic()


    