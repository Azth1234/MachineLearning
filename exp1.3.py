import pandas as pd
data = {
"Roll No": [101, 102, 103, 104, 105],
"Name": ["Ravi", "Priya", "Kiran", "Anu", "Sita"],
"Marks": [85, 92, 78, 88, 95]
}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)
print("\nFirst Three Records:")
print(df.head(3))
print("\nAverage Marks:")
print(df["Marks"].mean())
print("\nStudent with Highest Marks:")
print(df.loc[df["Marks"].idxmax()])
print("\nStudent with Lowest Marks:")
print(df.loc[df["Marks"].idxmin()])
def grade(mark):
         if mark >= 90:
             return "A"
         elif mark >= 80:
             return "B"
         else:
             return "C"
df["Grade"] = df["Marks"].apply(grade)
print("\nDataFrame with Grade:")
print(df)
