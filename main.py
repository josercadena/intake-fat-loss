# Static 
fit_index = {
	1: 1.2,
	2: 1.375,
	3: 1.55,
	4: 1.725,
	5: 1.9,
}

hb_constant = {
	"m": 5,
	"f": -161,
}

deficit = 500

# Basal Metabolic Rate or BMR
print("\nThis program determines BMR \n")

# Declaring variables 
name = input("Name: ")
sex = input("Sex (m or f): ")
age = int(input("Age: "))
weight = int(input("Weight (kg): "))
height = int(input("Height (cm): "))

# Determine Recommended Intake
fitness_level = int(input("Determine your level of Fitness: \n1: Little/no exercise \n2: Light exercise (1-3x/week) \n3: Moderate Exercise (3-5x/week) \n4: Heavy Exercise (6-7x/week) \n5: Very heavy exercise (twice per day) \n-> "))

# Compute Harris-Benedict equation
if (sex == "m" or sex == "f"):
	bmr = (10 * weight) + (6.25 * height) - (5 * age) + hb_constant.get(sex)
else:
	print("Invalid input")

print(bmr)

steady_intake = bmr * fit_index.get(fitness_level)
fat_loss_intake = steady_intake - deficit

print("Intake for fat loss: " + str(fat_loss_intake))
