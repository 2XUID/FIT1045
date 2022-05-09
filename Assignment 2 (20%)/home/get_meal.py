meal = ''
menu = []
#loop for split the meal variables and regroup
while meal!='.':
    meal = input()
    if meal != '.':
        x = meal.split(",")
        #regroup one single meal into dictionary form
        for i in x:
            if i.isdigit():
                i = float(i)
        thedist = {
            "name": x[0],
            "sell_for": float(x[1]),
            "cost_to_make": float(x[2]),
            "cook_time": float(x[3]),
            "cook_time_stdev": float(x[4])
        }
        #insert this meal into menu list
        menu.append(thedist)
print(menu)
