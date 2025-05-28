import random

grades = [round(random.uniform(1.0, 4.0), 1) for _ in range(20)]

# Divide the number of grades by the total number of students
participation = len(grades) / 76
