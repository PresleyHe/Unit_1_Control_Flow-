pin = 12344
PIN = str(pin)
i = 0
repeatingNum = False
while i < len(PIN)-1:
    num = PIN[i]
    next_num = PIN[i + 1]
    i += 1
    if next_num == num:
        repeatingNum = True
        break
if repeatingNum == True:
    print("No repeating digits!")
else:
    print("Pin valid!")