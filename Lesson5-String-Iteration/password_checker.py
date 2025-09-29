password = input("What is your password?:")
upperCaseCount = 0
lowercaseCount = 0
digitCount = 0
specialCharCount = 0

#Rating variable 
strength_Rate = 0

for char in password: 
    if "A" <= char <= "Z":
        upperCaseCount +=1
    if "a" <= char <= "z":
        lowercaseCount += 1
    if "0" <= char <= "9":
        digitCount += 1
    else:
        specialCharCount += 1
        
        
# Length check
if 0 < len(password) < 8:
         print(f"{password} is too short! 8 characters minimum❌!")
         strength_Rate -= 1
else:
         print(f"{password} is 8 characters minimum✅!")
         strength_Rate += 1
         
# Uppercase count
if upperCaseCount >= 1:
    print(f"{password} minimum of 1 uppercase letter ✅") 
    strength_Rate +=1 
else: 
        print(f"{password} minimum of 1 uppercase letter ❌") 
        
# lowercase count
if lowercaseCount >= 1:
    print(f"{password} minimum of 1 lowercase letter ✅") 
    strength_Rate += 1
else: 
        print(f"{password} minimum of 1 lowercase letter ❌")  

#digit count

if digitCount >= 1:
    print(f"{password} minimum of 1 digit ✅") 
    strength_Rate += 1
else: 
        print(f"{password} minimum of 1 digit❌")  
        
#Special character count
if specialCharCount >= 1:
    print(f"{password} minimum of 1 Special Character ✅") 
    strength_Rate += 1
else: 
        print(f"{password} minimum of 1 special character❌")  


# Each digit type count
print(
    "===========password character category count:========== \n"
    f"{password} character count: {len(password)}\n"
    f"{password} Uppercase count: {upperCaseCount} \n"
    f"{password} Lowercase count: {lowercaseCount} \n"
    f"{password} digit count: {digitCount} \n"
    f"{password} special character count: {specialCharCount}"
    
      )
#security vulnerabilities
# repeating characters 
for i in range(len(password) - 2): # Stop 2 before end
    if password[i] == password[i+1] == password[i+2]:
        print(f"Reapeating characters: {password[i]}")
        strength_Rate -= 1
#simple sequences
simple_sequences = ["123", "abc", "ABC", "abcd", "qwerty"]

for seq in simple_sequences:
    if seq in password:
        print(f"{password} has simple sequence!")
        strength_Rate -= 1

        

# Rate of strength
print(f"Strength rate:{strength_Rate}")
#strength rate 1-2: WEAK | 3: Normal | 4<=: STRONG
if strength_Rate <= 2: 
    print(f"{password} is WEAK!")
elif strength_Rate == 3:
    print(f"{password} is NORMAL!")
elif strength_Rate >= 4:
    print(f"{password} is STRONG!")
    
        