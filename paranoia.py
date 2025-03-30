import pandas as pd
import numpy as np
import requests
import json
import os

with open("student_directory.json", "r") as f:
    student_directory = json.load(f)

grade_input = str(input("Please enter the grade you want to filter by (e.g., '12'): "))
senior_data = []

for student in student_directory:
    if student["GradeDisplay"] == grade_input:
        senior_data.append({
            "Name": f"{student['FirstName']} {student['LastName']}",
            "Email": student["Email"]
        })

df = pd.DataFrame(senior_data)
print("Data successfully collected from student directory.")
print(f"First 5 entries: \n{df.head()} \n")

# Create third column for Paranoia targets
df['Paranoia Target'] = np.random.permutation(df['Name'].values)
print(f"First 5 entries with Paranoia Target: \n{df.head()} \n")
