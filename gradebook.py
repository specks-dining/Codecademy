last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 

# List of subjects
subjects = ["physics", "calculus", "poetry", "history"]

# List of grades
grades = [98, 97, 85, 88]

# List of grades in subjects
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

# Append new grade
gradebook.append(["computer science", 100])

gradebook.append(["visual arts", 93])

# Edit grade
gradebook[-1][-1] = 98

# Poetry grade change
gradebook[2].remove(85)
gradebook[2].append("Pass")

# Combine semester grades
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook)
