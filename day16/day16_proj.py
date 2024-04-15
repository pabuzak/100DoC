### module example ###
# import another_module
# print(another_module.another_variable)
#

### turtle ###
#from turtle import Turtle, Screen
#timmy = Turtle()
#print(timmy)
#timmy.shape("turtle")
#timmy.color('PaleGreen1')
#timmy.fd(100)

#my_screen = Screen()
#print(my_screen.canvheight)
#my_screen.exitonclick()


### prettytable ###
#from prettytable import PrettyTable
#table = PrettyTable()
#table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
#table.add_column("Type", ["Electric", "Water", "Fire"])
#table.align = "l"
 
#print(table)


### coffee machine ###
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

espresso = MenuItem("espresso", 50, 0, 18, 1.5)
latte = MenuItem("latte", 200, 150, 24, 2.5)
cappuccino = MenuItem("cappuccino", 250, 100, 24, 3.0)

menu = Menu()
maker = CoffeeMaker()

prompt_user = ""
while prompt_user != "off":
    prompt_user = input(f"What would you like? ({menu.get_items()}): ")
    drink = prompt_user
    if drink == "report":
        maker.report()
    elif drink == "off":
        break
    else:
        if menu.find_drink(drink):





