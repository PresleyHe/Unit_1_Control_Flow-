# pyramid pattern
# yaxis = 5
# xaxis = 4
# Spaces = 4
# rest = 1
# for y in range(yaxis):
#     for x in range(xaxis):
#         print(" " * Spaces + "*" * rest)
#         Spaces -= 1
#         rest += 2
#         break

rows = 5
# step 1: create an out loop for the rows
for i in range(rows):
    # Step 2: print the spaces rows - i -1
    for j in range(rows -i -1):
        print(" ", end="")
    #step3: print the stars 2*1+1
    for k in range(2*i+1):
        print("*", end="")
    #step4: print a new line
    print()