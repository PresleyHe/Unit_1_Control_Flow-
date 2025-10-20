username = input("What is your username:")
first_char = username[0]
starts_with_letter = ('a' <= username[0] <= "z") or ("A" <= username[0] <= "Z") 
validation = False
length = (6 <= len(username) <= 20)

if starts_with_letter and length: 
    validation = True
else:
    validation = False
        
print(f"Validation is {validation}")