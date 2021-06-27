# # import another_module
# # print(another_module.another_variable)
# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("DodgerBlue", "HotPink")
#
# timmy.forward(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"], align="l")
table.add_column("Type", ["Electric", "Water", "Fire"], align="l")
# table.align = 'l'

print(table)
