# pyramid pattern
yaxis = 9
xaxis = 5
Spaces = 4
rest = 1
for y in range(yaxis):
    for x in range(xaxis):
        print(" " * Spaces + "*" * rest)
        Spaces -= 1
        rest += 2
        break