# n = 4 
# spaces = n
# blocks = 1
# for rows in range(n):
#     for space in range(spaces):
#         print(" ", end="")
#     for block in range(blocks):
#         print("#", end="")
#     print()
#     blocks += 2
#     spaces -= 1

n = 4
spaces = n - 1
blocks = 1
for rows in range(n):
    for space in range(spaces):
        print(" ", end="")
    for block in range(blocks):
        print("#", end="")
    print()
    spaces -= 1
    blocks += 2