import pandas as pd

data = {
    "roll":[1,2,3,4,5],
     "Name": ["Anu", "Nikhil", "Neha", "Rahul", "Naveen"],
       "Age": [18, 19, 18, 20, 19],
       "Marks": [85, 75, 92, 68, 88]
}

df = pd.DataFrame(data)

# print(df)

print(df.head(2))

print(df[df["Marks"] > 80 ])

print(df[df["Name"].str.startswith("N")])

print(df['Age'].value_counts())

def calculate(mark):
    if mark > 80:
        return 'A+'
    elif mark > 70:
        return 'B+'
    else:
        return "F"

df["grade"] = df["Marks"].apply(calculate)

print(df[["Age","Marks"]])

print(df.groupby('Age')['Marks'].mean())