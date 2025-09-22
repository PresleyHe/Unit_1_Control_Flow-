height = float(input("height:"))
weight = float(input("weight:"))

BMI = (weight /(height ** 2)) * 703
category = ("Underweight" if BMI < 18.5 else
            "Normal" if 18.5 <= BMI <25 else
            "Overweight" if 25 <= BMI < 30 else
            "Obese" 
            )

print(f"BMI = {BMI} \n Category:{category}")