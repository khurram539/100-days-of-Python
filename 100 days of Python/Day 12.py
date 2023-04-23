# Day 12 - scope & number guessing game

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")
    
increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope

def drink_potion():
    potion_strength = 2
    print(potion_strength)
drink_potion()

drink_potion
#print(potion_strength)

# global scope

player_health = 10

def game ():
    def drink_potion():
        potion_strength = 2
        print(player_health)
    drink_potion()
print(player_health)


# Block scope

game_level = 3
def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]
    print(new_enemy)
create_enemy()

# Modifying global scope

enemies = 1

def increase_enemies():
    print(f"enemies inside function: {enemies}")
    return enemies + 1
enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

# Constants and global scope

pi = 3.14159
url = "https://www.google.com"
twitter_handle = "@yu_angela"


# The number guessing game

