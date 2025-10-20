# balance = 0
# vending_machine = (f"Item purchased! \n balance: ${balance - 2}" if balance >= 2 else "Not enough money!")
# print(vending_machine)


# count from 0 - 4
# for i in range(5):
#     print(i)
#Or make it count from 1-5
# for i in range(1,6):
#     print(i)
#Or make it count backwards from 10 - 0
# for i in range(10,-1,-1): #remember the first number is inclusive, the second one is exclusive
#     print(i)
#Or you could use this to run a loop based on every character in a string
# word = "hello"
# for char in word:
#     print(char)
#or use the range for checking each character
# for i in range(len(word)):#Makes sure that the digits are the same as the length of the string so it can be used for index numbers
    # print(word[i])#This makes it print the index number of the length which accurately picks out the characters
    
# n = 5
# safe = 0
# for rows in range(n):
#     for cols in range(n):
#         if cols == 0 or cols == n-1 or rows == 0 or rows == n-1:
#             print("X", end="")
#         else:
#             print("0",end="")
#             safe += 1
#     print()
# print(f"safes:{safe}")

# pts = 100
# lvl = 1

# while lvl < 5:
#     pts += lvl * 10
#     lvl += 1
#     if pts > 130:
#         lvl += 1

# print(lvl)
# total = 0
# months = 0
# while True:
#     Cost = int(input("Cost:"))
#     if Cost == -1:
#         break
#     if Cost < 5 or Cost > 50:
#         print("Invalid")
#         continue
#     total += Cost
#     months += 1
# print(f"The cost is {total} for {months} months")
    
# password = "SecurePass99"
# length = False
# upper = 0
# lower = 0
# digit = 0
# strong = False
# Weak = False
# if 8 <= len(password) <= 16:
#     length = True
# for char in password:
#     if "A"<= char <= "Z":
#         upper += 1
#     elif "a"<= char <= "z":
#         lower += 1
#     elif "0" <= char <= "9":
#         digit += 1

# if length and upper > 0 and lower > 0 and digit >= 2:
#     strong = True
# if strong:
#     print("Password is Strong")
# else:
#     print("Password is Weak")
# total = 0

# for squad in range(3):
#     for player in range(4):
#         total += 1
#         if total >= 10:
#             break

# print(total)