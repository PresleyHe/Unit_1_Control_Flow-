# JS Ternary
''' 

let status = age >= 18 ? "adult" : "minor"
let message = score >= 90 ? "Excellent" : "Keep Trying"
'''

#Python Ternary
age = 15
status = "adult" if age >= 18 else "minor"
score = 75 
message = "excellent" if score  >=90 else "Keep Trying!"

#Examples 
password = "mypass123"
strength = "Strong Password!" if len(password) >= 8 else "Weak Password!!!"
print(f"Password:{password}\n Strength:{strength}")

#combining ternary + chaining
category = ("Child" if 0<= age <= 12 else
            "teen" if 13 <= age <= 17 else
            "adult" if 18<= age <= 64 else
            "senior"
            )

score = 89
grade = ("A" if 90 <= score <= 100 else
         "B" if 80 <= score <= 89 else
         "C" if 70 <= score <= 79 else
         "D" if 60 <= score <= 69 else
         "F"
         )
print(f"Score:{score} \n grade:{grade}")