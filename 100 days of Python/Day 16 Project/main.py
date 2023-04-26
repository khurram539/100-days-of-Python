# Day 16 - Oject Oriented Programming 



#import another_module

#print(another_module.another_variable)

#from turtle import turtle
#timmy = turtle()

#print(timmy)
#timmy.shape("turtle")
#timmy.color("coral")
#timmy.forward(100)


#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()


#print(" | Pokemon | type | HP | Attack | Defense | Special Attack | Special Defense | Speed |")
#print(" | Bulbasaur | Grass | 45 | 49 | 49 | 65 | 65 | 45 |")
#print(" | Charmander | Fire | 39 | 52 | 43 | 60 | 50 | 65 |")
#print(" | Squirtle | Water | 44 | 48 | 65 | 50 | 64 | 43 |")

# Coffee Machine in OOP

from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
          coffee_maker.make_coffee(drink)