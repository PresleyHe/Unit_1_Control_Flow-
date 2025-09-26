# String indexing 
# ======================
word = "Python"
#       012345(Positive Indexing)
word[0] #P (First Character)
word[1] #Y (Second character)
word[5] #n (last character)
word[-1] #n (last character)
len(word) #length on the string
word[len(word)-1]#n last character
#String Slicing
# =========================
word[0:3] #Pyt (characters 0,1,2)
word[:3] #Pyt (characters 0,1,2)
word[2:6] #tho (characters 2,3,4,5)
word[2: len(word)] #tho (characters 2,3,4,5)
word[2:] #tho (characters 2,3,4,5)
word[-3] #hon (characters -3,-2,-1 or 3,4,5)

#Part 1-String Iteration Patterns
# Direct Character Iteration
word = 'hello'

for char in word:
    print(char)

# Index based Iteration
for i in range(len(word)):
    print(f"Character {i}: {word[i]}")
    
# Character Classification
char = input("Press a Key:")
#Check character types using ASCII ranges
if 'A' <= char <= 'Z':
    print(f"'{char} is uppercase'")
if 'a' <= char <= 'z':
    print(f"'{char} is lowercase'")
if '0' <= char <= '9':
    print(f"'{char} is a digit'")
if 'a' <= char <= 'z' or  'A' <= char <= 'Z':
    print(f"{char} is a letter")
