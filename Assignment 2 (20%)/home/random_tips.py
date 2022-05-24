import random
#input average cook time and the standard deviation
cook_time = int(input("input correct time: "))
stdev = int(input("input standard deviation: "))
#random real cooking time and set up tip_rate
real_cook_time = random.gauss(cook_time,stdev)
tip_rate = 0
#using decision-making structure decide tip rate
if(real_cook_time<cook_time-2*stdev):
    tip_rate = -5
elif(real_cook_time>=cook_time-2*stdev and real_cook_time<cook_time-stdev):
    tip_rate = 0
elif(real_cook_time>=cook_time-stdev and real_cook_time<cook_time+stdev):
    tip_rate = 5
elif(real_cook_time>=cook_time+stdev and real_cook_time<cook_time+2*stdev):
    tip_rate = 0
elif(real_cook_time>cook_time+2*stdev):
    tip_rate = -5
print("Actual cooking time was "+str(real_cook_time)+" and the tip paid was "+str(tip_rate)+"%")