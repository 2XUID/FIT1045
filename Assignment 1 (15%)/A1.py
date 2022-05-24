#part1
new_row=input()                           #Input
current_row = "1112221\n2211122\n1112221" #Prepare current existing row
print(new_row,"\n",current_row)           #Print the input row first with new line, then print rest of row
#part2
num=int(input())        #input number
answer=0
counter=1               #counter start with 1
i=6                     #the last number location is 6
while(i>=0):            #the first location of digit is 0 for computer, start with 0
    number = num//10**i%10
    if(counter==5):
        answer = number #using buffer to record the fifth digit of number
    counter=counter+1
    i=i-1
print(answer)
#part3
index = int(input())        #the first of these represents the column number
num = int(input())          #this second represents the 7-digit number to explore
counter=0
answer=0
i=6                         #due to the index is count from left to right we start at 7
while(i>-1):                #decreae to 0 (the last number position is 0 not 1)
    number = num//10**i%10  #get the number in position
    if(counter==index-1):   #match the position with user indicate position(index count start with 1)
        answer = number     #get the number of that column
    counter=counter+1       #column number add one
    i=i-1
print(answer)
#part4
row = int(input())          #input the row
num = int(input())          #this second represents the 7-digit number to explore
index = int(input())        #the first of these represents the column number
counter=0
answer=0
i=6                         #due to the index is count from left to right we start at 7
while(i>-1):                #decreae to 0 (the last number position is 0 not 1)
    number = row//10**i%10  #get the number in position
    if(counter==index-1):   #match the position with user indicate position(index count start with 1)
        answer = number     #get the number of that column
    counter=counter+1       #column number add one
    i=i-1
if(answer == 0):            #if the position have space fr player add player
    new_number = row+num*10**(7-index)
    print(new_number)
else:                       #else no space
    print("invalid move")
#part5
index = int(input())               #the first of these represents the column number
counter = 1                        #counter represent the available position
for i in range(6):
    row = int(input())             #input the row
    number = row//10**(7-index)%10 #check the number of column we indicate
    if number != 0:                #if the number is not 0, that mean there are no space for the player
        counter = counter+1        #position+1 and next row input we check next row
if counter == 7:                   #while the position reach 7 that mean in this column there are no space for player
    print('no room in column', index)
else:                              #if counter is not 7 that mean there are a space for player and the position is the value of counter
    print(counter)
#part6
row = int(input())            #input the row
player = int(input())         #tell the program which player gonna be check
counter = 0
for i in range(6):            #check the number inside the row one by one
    number = row//10**i%10
    if number == player:      #if it is player counter + 1
        counter = counter+1
    elif(counter<4):          #if the player cannnot reach 4 combo and cut by other, then set counter to 0
        counter = 0
if(counter>=4):               #when player reach 4 combo or more than 4, then he win
    print(True)
else:
    print(False)              #when player cannot reach 4 combo then he does not win yet
#part7
player = int(input())              #tell the program which player gonna be check
index = int(input())               #the first of these represents the column number
counter = 0
for i in range(6):
    row = int(input())
    number = row//10**(7-index)%10 #check the column is the player or not
    if number == player:           #if it is player counter + 1
        counter = counter+1
    elif(counter<4):               #if the player cannnot reach 4 combo and cut by other, then set counter to 0
        counter = 0
if(counter>=4):                    #when player reach 4 combo or more than 4, then he win
    print(True)
else:
    print(False)                   #when player cannot reach 4 combo then he does not win yet