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
