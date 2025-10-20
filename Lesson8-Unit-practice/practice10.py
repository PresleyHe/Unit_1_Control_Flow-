validation = False
while not validation:
    hours = int(input("How many hours have you watched?:"))
    if 1 <= hours <= 24:
        validation = True
    else:
        print("Invalid hours!")
print(validation)