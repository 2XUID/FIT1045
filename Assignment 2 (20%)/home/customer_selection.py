#set up variables
counter = 1
meal = ''
default_menu = [{'name': 'Budda Bowl (vg)', 'sell_for': 25.0, 'cost_to_make': 20.0, 'cook_time': 10.0, 'cook_time_stdev': 3.0}, {'name': 'Eye Fillet Steak', 'sell_for': 55.0, 'cost_to_make': 25.0, 'cook_time': 7.0, 'cook_time_stdev': 1.0}, {'name': 'Spaghetti Bolognese', 'sell_for': 30.0, 'cost_to_make': 22.0, 'cook_time': 40.0, 'cook_time_stdev': 5.0}, {'name': 'Pad Thai (seafood)', 'sell_for': 22.0, 'cost_to_make': 17.0, 'cook_time': 30.0, 'cook_time_stdev': 1.0}]
menu = []
flag = True
#loop for split the meal variables and regroup
while meal!='.':
    meal = input()
    if meal != '.':
        x = meal.split(",")
        thedist = {
            "name": x[0],
            "sell_for": float(x[1]),
            "cost_to_make": float(x[2]),
            "cook_time": float(x[3]),
            "cook_time_stdev": float(x[4])
        }
        menu.append(thedist)
        flag = False
#if user input "." in the beginning, flag keeps True,using default menu
if flag:
    #let user input the meal selection
    selection = input()
    #check input is digit or not, and check if the user selection is ourside of range
    if selection.isdigit() and int(selection)<= len(default_menu) and int(selection)>0:
        #print result
        print("now cooking "+ default_menu[int(selection)-1]["name"])
    else:
        #print error
        print("invalid choice")
else:
#else using menu their input
    selection = input()
    if selection.isdigit() and int(selection)<= len(menu) and int(selection)>0:
        print("now cooking "+ menu[int(selection)-1]["name"])
    else:
        print("invalid choice")