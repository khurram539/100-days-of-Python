# Day 14 - Higher Lower Game

from art import logo
from game_data import data

print (logo)

account_a = random.choice(data)
account_b = random.choice(data)
if account_a == account_b:
    account_b = random.choice(data)
    
account_name = account_a["name"]
account_descr = account_a["description"]
account_country = account_a["country"]



