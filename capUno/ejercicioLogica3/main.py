# program that creates a Body mass index (BMI), 
# Formula = BMI = weight / (height ^ 2)

weight = float(input("Enter your weight in Kilograms: "))

height = float(input("Enter your height in meters: "))

BMI = weight / (height ** 2)

print(f"Your BMI is: {BMI:.2f}")