#Default menu used for testing
default_menu = [{'name': 'Budda Bowl (vg)', 'sell_for': 25.0, 'cost_to_make': 20.0, 'cook_time': 10.0, 'cook_time_stdev': 3.0}, {'name': 'Eye Fillet Steak', 'sell_for': 55.0, 'cost_to_make': 25.0, 'cook_time': 7.0, 'cook_time_stdev': 1.0}, {'name': 'Spaghetti Bolognese', 'sell_for': 30.0, 'cost_to_make': 22.0, 'cook_time': 40.0, 'cook_time_stdev': 5.0}, {'name': 'Pad Thai (seafood)', 'sell_for': 22.0, 'cost_to_make': 17.0, 'cook_time': 30.0, 'cook_time_stdev': 1.0}]
import random
def get_meals_list_from_user():
    '''
    Takes the input from the user and organises it into a
    list of dictionaries containing the info on the menu
    INPUT:
        Null
    OUTPUT:
        A list of dictionaries
    '''
    #Variables
    meal = ''
    menu = []
    #Splits the string and organises the input into dictionaries
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
    #checks if there was an input, if not returns the default menu
    if len(menu) == 0:
        return default_menu
    else:
        return menu

def display_menu(options):
    '''
    Formats a list of dictionaries into a user friendly menu
    INPUT:
        options --> A list of dictionaries formatted such as an output of get_meals_list_from_user()
    OUTPUT:
        A series of print statements
        Returns None
    '''
    counter = 1
    #Iterates through dictionaries and formats them correctly
    for item in options:
            print(str(counter)+"."+" Name:"+item["name"]+" Sells:$"+str(item["sell_for"])+" Costs:$"+str(item["cost_to_make"])+" Takes:"+str(item["cook_time"])+" mins")
            counter += 1
    return


def validate_user_choice(options,users_input):
    '''
    Validates that an input or choice given by the customer or user is a valid item on the menu
    INPUT:
        options --> a list of dictionaries formatted such as an output of get_meals_list_from_user()
        users_input --> a string
    OUTPUT:
        Boolean
    '''
    #Checks that users input contains only integers
    if users_input.isdigit()==False:
        return False
    #Changes users_input from string to integer
    users_input = int(users_input)
    #Checks if users_input is in list of options
    if users_input > len(options):
        return False
    else:
        return True

def classify_cook_time(average_cook_time, stdev_cook_time, actual_cook_time):
    '''
    Classifies the quality of the 'meal' based on 'cook time' vs 'average cook time'
    INPUT:
        average_cook_time --> float
        stdev_cook_time --> float
        actual_cook_time --> float
    OUTPUT:
        String, one of five category
    '''
    #Checks to see what field the actual_cook_time falls within
    if actual_cook_time < average_cook_time - 2*stdev_cook_time:
        return "very undercooked"
    elif actual_cook_time >= average_cook_time - 2*stdev_cook_time and actual_cook_time <= average_cook_time - stdev_cook_time:
        return "slightly undercooked"
    elif actual_cook_time > average_cook_time-stdev_cook_time and actual_cook_time < average_cook_time + stdev_cook_time:
        return "well cooked"
    elif actual_cook_time >= average_cook_time + stdev_cook_time and actual_cook_time <= average_cook_time + 2*stdev_cook_time:
        return "slightly overcooked"
    elif actual_cook_time > average_cook_time + 2*stdev_cook_time:
        return "very overcooked"


def get_cooking_tip(classification,base_tip):
    '''
    Uses 'meal quality' to assign 'tip' values
    INPUT:
        classification --> String, output of classify_cook_time
        base_tip --> float
    OUTPUT:
        float
    '''
    #Assigns value according to classification
    if classification == 'very undercooked':
        return -100
    elif classification == 'slightly undercooked':
        return 0
    elif classification == 'well cooked':
        return base_tip
    elif classification == 'slightly overcooked':
        return 0
    elif classification == 'very overcooked':
        return -100

def random_tip_compute(tip_chance, base_tip_value, random_comparison):
    '''
    Compares the chance of a tip vs a randomly generated number to calculate the final tip
    INPUT:
        tip_chance --> float
        base_tip_value --> float
        random_comparison --> float
    OUTPUT:
        float
    '''
    #calculate tips in different situation
    if random_comparison < tip_chance:
        return base_tip_value
    elif random_comparison > (1-tip_chance):
        return base_tip_value*-1
    else:
        return 0.0

def order(options):
        validatation = False
        #display menu
        print('Please enter your order. The options are given below')
        display_menu(options)
        print('Please enter a number to make your choice')
        #Variables check
        while validatation == False:
            #Prints the menu and takes user choice
            choice = input()
            validatation = validate_user_choice(options, choice)
            if validatation == False:
                print("Your order is not on our menu, please pick something from our menu")
        #define variables
        menu_choice = options[int(choice)-1]
        name = menu_choice["name"]
        price = menu_choice["sell_for"]
        cost = menu_choice["cost_to_make"]
        time_to_make = menu_choice["cook_time"]
        sd_time_to_make = menu_choice ["cook_time_stdev"]
        repeat_counter=1
        total_profit = 0
        #initial cooking level is very overcooked in order to go in while loop
        cook_level = 'very overcooked'
        #if cook_level is 'very overcooked' or 'very undercooked' or repeat counter is not reach 3 times, then recook
        while (cook_level=='very overcooked'or cook_level=='very undercooked') and repeat_counter<=3:
        #Classify cook time
            random_rate = random.random()
            real_cook_time = random.gauss(time_to_make,sd_time_to_make*2)
            cook_time = random.gauss(time_to_make,sd_time_to_make)
            cook_level = classify_cook_time(cook_time,sd_time_to_make,real_cook_time)
            tip = get_cooking_tip(cook_level,base_tip = 10)
            #calculate ramdom_tip
            ramdom_tip = random_tip_compute(0.1,5,random_rate)
            #Print result
            print("Now cooking", name)
            print(name, 'was ',cook_level,'(',round(cook_time,2),'vs',round(real_cook_time,2),' mins)')
            print("cooking tip was ",tip,"random tip was ",ramdom_tip," the random value being (",round(random_rate,2),")")
            #Calculate selling price
            if tip == -100:
                selling_price = 0.00
            else:
                selling_price = price+price*(tip/100)
            #calculate and print profit
            profit = selling_price-cost+ramdom_tip
            total_profit = total_profit+profit
            #turn profit into string
            if profit<0:
                str_profit = "-$"+str(-profit)
            else:
                str_profit = "$"+str(profit)
            print("final selling price was $", selling_price)
            print("for a profit of ",str_profit)
            #counter +1
            repeat_counter+=1
        # show it while after the recook is over 3 and still mess up
        if(repeat_counter==4 and (cook_level=='very overcooked'or cook_level=='very undercooked')):
            print("giving up after ", repeat_counter-1 ," failed attempts")
            print("overall, the profit for this meal was", total_profit,"$")
        return total_profit

#This function for R9
def order_for_x_people(number):
    total_profit = 0.0
    if number.isdigit():
        number = int(number)
        str_number = str(number)
        options = get_meals_list_from_user()
        while number >0:
            validatation = False
            #display menu
            print('Please enter your order. The options are given below')
            display_menu(options)
            print('Please enter a number to make your choice')
            #Variables check
            while validatation == False:
                choice = input()
                validatation = validate_user_choice(options, choice)
                if validatation == False:
                    print("Your order is not on our menu, please pick something from our menu")
            #Prints the menu and takes user choice
            menu_choice = options[int(choice)-1]
            name = menu_choice["name"]
            price = menu_choice["sell_for"]
            cost = menu_choice["cost_to_make"]
            time_to_make = menu_choice["cook_time"]
            sd_time_to_make = menu_choice ["cook_time_stdev"]
            repeat_counter=1
            cook_level = 'very overcooked'
            meal_profit = 0
            while (cook_level=='very overcooked'or cook_level=='very undercooked') and repeat_counter<=3:
            #Classify cook time
                random_rate = random.random()
                real_cook_time = random.gauss(time_to_make,sd_time_to_make*2)
                cook_time = random.gauss(time_to_make,sd_time_to_make)
                cook_level = classify_cook_time(cook_time,sd_time_to_make,real_cook_time)
                tip = get_cooking_tip(cook_level,base_tip = 10)
                #calculate ramdom_tip
                ramdom_tip = random_tip_compute(0.1,5,random_rate)
                #Print cooking result
                print("Now cooking", name)
                print(name, 'was ',cook_level,'(',round(cook_time,2),'vs',round(real_cook_time,2),' mins)')
                print("cooking tip was ",tip,"random tip was ",ramdom_tip," the random value being (",round(random_rate,2),")")
                #Calculate selling price
                if tip == -100:
                    selling_price = 0.00
                else:
                    selling_price = price+price*(tip/100)
                #calculate and print profit
                profit = selling_price-cost+ramdom_tip
                #calculate the profit per meal
                meal_profit = meal_profit+profit
                #calculate total profit of total meal
                total_profit = total_profit+profit
                #turn profit into string
                if profit<0:
                    str_profit = "-$"+str(-profit)
                else:
                    str_profit = "$"+str(profit)
                #print profit per cooking result
                print("final selling price was $", selling_price)
                print("for a profit of ",str_profit)
                repeat_counter+=1
            # show it while after the recook is over 3 and still mess up
            if(repeat_counter==4 and (cook_level=='very overcooked'or cook_level=='very undercooked')):
                print("giving up after ", repeat_counter-1 ," failed attempts")
            #print profit per meal result
            print("overall, the profit for this meal was", meal_profit,"$")
            print("running profit: $", total_profit)
            number = number-1
        #print profit total result
        print("After serving meals to "+str_number+" people, ", "we made a profit of $ ",total_profit)
        return total_profit


if __name__ == "__main__":
    #order(get_meals_list_from_user())
    order_for_x_people(input("input the number: "))