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
    #user input a set of number
    theSet = input().split(",")
    #the real cook time index is 1
    real_cook_time = float(theSet[1])
    #get information from menu
    mealName=default_menu[int(theSet[0])-1]["name"]
    cook_time = default_menu[int(theSet[0])-1]["cook_time"]
    stdev = default_menu[int(theSet[0])-1]["cook_time_stdev"]
    #calculate the range of cooking level and print out
    if(real_cook_time<cook_time-2*stdev):
        print(mealName+" was very undercooked and cooking tip was -100%")
    elif(real_cook_time>=cook_time-2*stdev and real_cook_time<cook_time-stdev):
        print(mealName+" was slightly undercooked and cooking tip was 0%")
    elif(real_cook_time>=cook_time-stdev and real_cook_time<cook_time+stdev):
        print(mealName+" was well cooked and cooking tip was 10%")
    elif(real_cook_time>=cook_time+stdev and real_cook_time<cook_time+2*stdev):
        print(mealName+" was slightly overcooked and cooking tip was 0%")
    elif(real_cook_time>cook_time+2*stdev):
        print(mealName+" was very overcooked and cooking tip was -100%")
else:
    theSet = input().split(",")
    real_cook_time = float(theSet[1])
    mealName=menu[int(theSet[0])-1]["name"]
    cook_time = menu[int(theSet[0])-1]["cook_time"]
    stdev = menu[int(theSet[0])-1]["cook_time_stdev"]
    if(real_cook_time<cook_time-2*stdev):
        print(mealName+" was very undercooked and cooking tip was -100%")
    elif(real_cook_time>=cook_time-2*stdev and real_cook_time<cook_time-stdev):
        print(mealName+" was slightly undercooked and cooking tip was 0%")
    elif(real_cook_time>=cook_time-stdev and real_cook_time<cook_time+stdev):
        print(mealName+" was well cooked and cooking tip was 10%")
    elif(real_cook_time>=cook_time+stdev and real_cook_time<cook_time+2*stdev):
        print(mealName+" was slightly overcooked and cooking tip was 0%")
    elif(real_cook_time>cook_time+2*stdev):
        print(mealName+" was very overcooked and cooking tip was -100%")