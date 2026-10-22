
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('students_data.csv')
print(df)


print("\n First 2 Students ")
print(df.head(2))


print("\n Total Number of Students ")
print(len(df))


print("\n Students in Each Department ")
print(df['dep'].value_counts())


print("\n Students Scoring Above 60 ")
print(df[df['marks'] > 60])


df['marks'] = df['marks'].fillna(df['marks'].mean())

print("\n Data After Filling Missing Marks ")
print(df)


def calculate(mark):
    if mark > 80:
        return 'A+'
    elif mark > 70:
        return 'B+'
    elif mark > 60:
        return 'C+'
    else:
        return 'F'

df['Grade'] = df['marks'].apply(calculate)

print("\n Student Grades ")
print(df[['name', 'marks', 'Grade']])


print("\n Average Marks by Department ")
print(df.groupby('dep')['marks'].mean())


high_scorers = df[df['marks'] >= 50]
high_scorers.to_csv('high_scorers.csv', index=False)

print("\n CSV File Saved Successfully ")
print("Filename: high_scorers.csv")
print("Number of students saved:", len(high_scorers))



df['dep'].value_counts().plot(kind='bar')

plt.title('Number of Students per Department')
plt.xlabel('Department')
plt.ylabel('Number of Students')
plt.show()

# OUTPUT
#         name  dep  marks
# 0    Abinson  MCA   55.0
# 1  Ashwameth  ECE   65.0
# 2      Rahul  CSE   70.0
# 3      Arjun  MCA    NaN
# 4      Akhil  CSE   85.0
# 5        Anu  ECE   92.0
# 6       Neha  MCA   48.0
# 7       Amal  CSE   76.0
# 8      Sneha  ECE    NaN

#  First 2 Students 
#         name  dep  marks
# 0    Abinson  MCA   55.0
# 1  Ashwameth  ECE   65.0

#  Total Number of Students 
# 9

#  Students in Each Department 
# dep
# MCA    3
# ECE    3
# CSE    3
# Name: count, dtype: int64

#  Students Scoring Above 60 
#         name  dep  marks
# 1  Ashwameth  ECE   65.0
# 2      Rahul  CSE   70.0
# 4      Akhil  CSE   85.0
# 5        Anu  ECE   92.0
# 7       Amal  CSE   76.0

#  Data After Filling Missing Marks 
#         name  dep      marks
# 0    Abinson  MCA  55.000000
# 1  Ashwameth  ECE  65.000000
# 2      Rahul  CSE  70.000000
# 3      Arjun  MCA  70.142857
# 4      Akhil  CSE  85.000000
# 5        Anu  ECE  92.000000
# 6       Neha  MCA  48.000000
# 7       Amal  CSE  76.000000
# 8      Sneha  ECE  70.142857

#  Student Grades 
#         name      marks Grade
# 0    Abinson  55.000000     F
# 1  Ashwameth  65.000000    C+
# 2      Rahul  70.000000    C+
# 3      Arjun  70.142857    B+
# 4      Akhil  85.000000    A+
# 5        Anu  92.000000    A+
# 6       Neha  48.000000     F
# 7       Amal  76.000000    B+
# 8      Sneha  70.142857    B+

#  Average Marks by Department 
# dep
# CSE    77.000000
# ECE    75.714286
# MCA    57.714286
# Name: marks, dtype: float64

#  CSV File Saved Successfully 
# Filename: high_scorers.csv
# Number of students saved: 8