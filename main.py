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

# Deficit recommended 350 or 500
deficit = 500

# Energy density of each macro:
protein_cals_gram = 4
carbs_cals_gram = 4
fat_cals_gram = 9

# Recommended gr protein per pound of bodyweight
protein_index = {
	1: 0.7,
	2: 1,
	3: 1.2,
	4: 1.5,
}

# Recommended gr fat per pound of bodyweight
fat_index = {
	1: 0.25,
	2: 0.30,
	3: 0.40,
}

# Basal Metabolic Rate or BMR
print("\nThis program determines BMR \n")

# Declaring variables 
name = input("Name: ")
sex = input("Sex (m or f): ")
age = int(input("Age: "))
weight = int(input("Weight (kg): "))
height = int(input("Height (cm): "))

# Determine current level and goals
fitness_level = int(input("\nDetermine your level of Fitness: \n1. Little/no exercise \n2. Light exercise (1-3x/week) \n3. Moderate Exercise (3-5x/week) \n4. Heavy Exercise (6-7x/week) \n5. Very heavy exercise (twice per day) \n-> "))
protein_goal = int(input("\nDetermine your goals: \n1. Healthy sedentary adult. No workout \n2. Doing some form of exercise or trying to improve their body \n3. Trying to get toned, lose fat, increase strength and improve performance \n-> "))
fat_goal = int(input("\nDetermine your rate: \n1. Short term: contest preparation, photo-shoot preparation \n2. Moderate and reasonable rate, without being too fast \n3. Moderate yet longer approach, not compromising satiety. For long-term lifestyle change \n-> "))

# Compute Harris-Benedict equation
if (sex == "m" or sex == "f"):
	bmr = (10 * weight) + (6.25 * height) - (5 * age) + hb_constant.get(sex)
else:
	print("Invalid input")

# Compute recommended intake for fat loss
maximum_intake = bmr * fit_index.get(fitness_level)
total_intake_for_fat_loss = maximum_intake - deficit

# Compute protein and fat intake
if (protein_goal == 3):
	if (sex == "m"): 
		# Index for male
		protein_intake = (protein_index.get(4)*2.2) * weight # 2.2: Pound-gram; 1000: kg-gram
	else:
		# Index for female
		protein_intake = (protein_index.get(3)*2.2) * weight
else: 
	protein_intake = (protein_index.get(protein_goal)*2.2) * weight 

fat_intake = (fat_index.get(fat_goal)*2.2) * weight

# Compute calories for protein and fat intakes
protein_intake_calories = protein_intake * protein_cals_gram
fat_intake_calories = fat_intake * fat_cals_gram

# Compute calories available for carbs
carbs_intake_calories = total_intake_for_fat_loss -protein_intake_calories - fat_intake_calories
carbs_intake = carbs_intake_calories/carbs_cals_gram


print("\nBMR: " + str(bmr))
print("Intake for fat loss: " + str(total_intake_for_fat_loss))
print("\nRecommended macro intake: \n")
print(" Protein: " + '{0:.4g}'.format(protein_intake) + " gr")
print(" Carbs: " + '{0:.4g}'.format(carbs_intake) + " gr")
print(" Fat: " + '{0:.4g}'.format(fat_intake) + " gr")
