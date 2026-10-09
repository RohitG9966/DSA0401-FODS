import numpy as np

student_scores = np.array([
    [85, 90, 78, 80],
    [88, 85, 82, 75],
    [92, 95, 80, 85],
    [80, 88, 85, 78]
])

subjects = ["Math", "Science", "English", "History"]

avg = np.mean(student_scores, axis=0)

print("Average Marks:", avg)

i = np.argmax(avg)
print("Highest Average Subject:", subjects[i])
print("Highest Average:", avg[i])
