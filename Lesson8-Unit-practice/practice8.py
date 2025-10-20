password = "1oDoooooo"
validation = False
uppercase = False
digit = False
for char in password:
    if "A" <= char <= "Z":
        uppercase = True
    if "0" <= char <= "9":
        digit = True
if len(password) >= 8 and uppercase and digit:
    validation = True
else:
    validation = False
print(validation)