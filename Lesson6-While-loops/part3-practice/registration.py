# part1
while True:
    hasSpace = False
    username = input("Enter a username:")
    for char in username:
        if char == " ":
            print("You cannot have spaces!")
            hasSpace = True
            break
    if hasSpace == True:
        continue
    if len(username) < 3:
        print("Too short!")
        continue
    if len(username) > 15:
        print("Too long!")
        continue
    break

    
        
# part2:

while True:
    hasSpace = False
    isUpper = False
    isDigit = False
    password = input("Enter a password:")
    for char in password:
        if char == " ":
            print("You cannot have spaces!")
            hasSpace = True
            break
    if len(password) < 8:
        print("Too short!")
        continue
    for char in password:
        if char.isupper():
            isUpper = True
            continue
        if char.isdigit():
            isDigit = True
            continue
    if isDigit == False:
        print("You need a digit!")
        continue
    if isUpper == False:
        print("You need a uppercase character!")
        continue
    # print("Password valid!")
    break

#3
while True:
    isaDigit = True
    age = input("What is your age?:")
    for char in age:
        if not char.isdigit():
            print("Your age needs to be only a number!")
            isaDigit = False
            break
    if isaDigit == False:
        continue
    if isaDigit == True:
        age = int(age)
        # print(type(age))
    if age < 13:
        print("Too young!")
        continue
    if age > 120:
        print("Too old!")
        continue
    # print(f"Your age is {age}")
    break

#4
while True:
    Yes = False
    No = False
    ask = input("Submit information? Yes or No?:").upper()
    if ask == "Y" or ask == "YES":
        Yes = True
        print(f"Registration complete \n Username:{username} \n Password: {password} \n Age: {age}")
    if ask == "N" or ask == "NO":
        No = True
        print("Registration cancelled!")
    if Yes == False and No == False: 
        print("Please enter yes/y or no/n!")
        continue
    break
