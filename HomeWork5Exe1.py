name = input("Enter first name: ")
grade = input("Enter grades: ")

mutasion_name = name.capitalize()
mutasion_grade = grade.upper()

print("Hi " + mutasion_name + " your grades are :"  + mutasion_grade)

num_grades = len(mutasion_grade)
print(" You have " + str(num_grades)+ "grades")

second_grade = mutasion_grade[1]
print(" Your grade for the second course is :"+ second_grade)

count_A_to_B = mutasion_grade.count('A') + mutasion_grade.count('B')
print("The number of A's and B's is: " + str(count_A_to_B))
