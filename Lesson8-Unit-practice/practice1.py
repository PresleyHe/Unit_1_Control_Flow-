age = int(input("Please enter an age:"))
if age < 13:
    price = 8
    print(f"Price: ${price}")
elif 13 <= age <=64:
    price = 15
    print(f"Price: ${price}")
else:
    price = 10
    print(f"Price: ${price}")