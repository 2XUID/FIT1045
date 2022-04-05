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
        #regroup into dictionary form
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
    for item in default_menu:
        print(str(counter)+"."+" Name:"+item["name"]+" Sells:$"+str(item["sell_for"])+" Costs:$"+str(item["cost_to_make"])+" Takes:"+str(item["cook_time"])+" mins")
        counter +=1
else:
#else using menu their input
    for item in menu:
        print(str(counter)+"."+" Name:"+item["name"]+" Sells:$"+str(item["sell_for"])+" Costs:$"+str(item["cost_to_make"])+" Takes:"+str(item["cook_time"])+" mins")
        counter +=1
