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


menu = Menu()
maker = CoffeeMaker()
money = MoneyMachine()

prompt_user = ""
while prompt_user != "off":
    prompt_user = input(f"What would you like? ({menu.get_items()}): ")
    if prompt_user == "report":
        maker.report()
        money.report()
    elif prompt_user == "off":
        break
    else:
        drink = menu.find_drink(prompt_user)
        if drink and maker.is_resource_sufficient(drink):
            money.make_payment(drink.cost)
            maker.make_coffee(drink)

                    



