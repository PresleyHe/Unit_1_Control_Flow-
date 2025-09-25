# Three froms of range() functions
#1 range(stop)
for i in range(5): # 0, 1, 2, 3, 4
    print(i)
#2 range(start, stop) # 3, 4, 5, 6, 7
for i in range(3,8):
    print(i)
#3 range(start, stop) # 3, 4, , 6, 7, 10
for i in range(3,11, 2):
    print(i)
    #counting backwards
for i in range(10, 1,-2):#10, 8, 6, 4, 2
    print(i)
#Countdown Timer
import time 
for seconds in range(10,-1,-1):
    print(f"{seconds} - seconds")
    # time.sleep(1) #wait 1 second between numbers
print("BLAST OFF🚀")

#Multiplication Table
#Take user input for the number and print the table number * 1 = number
#if the user submitted 5
# 5 * 1 = 5
# 5 * 2 = 10
user_input = int(input("Choose a number(1-12):"))
if 1 <= user_input <= 12:
    for num in range(0, 13):
        result = user_input * num
        print(f"{user_input} * {num:2d} = {result:3d}")
else:
    print("Please enter a number between 1-12")