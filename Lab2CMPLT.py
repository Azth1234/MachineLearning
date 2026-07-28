# ===============================
# EXPERIMENT 2 - Exploratory Data Analysis (EDA)
# ===============================

import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Task A: Dataset Loading and Inspection
# -------------------------------

df = pd.read_csv("data.csv")

print("\nFIRST FIVE RECORDS")
print(df.head())

print("\nLAST FIVE RECORDS")
print(df.tail())

print("\nROWS AND COLUMNS")
print(df.shape)

print("\nCOLUMN NAMES")
print(df.columns)

print("\nDATA TYPES")
print(df.dtypes)

print("\nDATASET INFORMATION")
print(df.info())

# -------------------------------
# Task B: Statistical Analysis
# -------------------------------

print("\nMean Attendance:", df["Attendance"].mean())
print("Average Internal Marks:", df["InternalMarks"].mean())
print("Average External Marks:", df["ExternalMarks"].mean())

print("Maximum Internal Marks:", df["InternalMarks"].max())
print("Minimum Internal Marks:", df["InternalMarks"].min())

print("Maximum External Marks:", df["ExternalMarks"].max())
print("Minimum External Marks:", df["ExternalMarks"].min())

print("Standard Deviation of Internal Marks:",
      df["InternalMarks"].std())

print("\nSummary Statistics")
print(df.describe())

# -------------------------------
# Task C: Data Manipulation
# -------------------------------

df["TotalMarks"] = df["InternalMarks"] + df["ExternalMarks"]

df["Percentage"] = (df["TotalMarks"] / 100) * 100

print("\nUPDATED DATAFRAME")
print(df)

# -------------------------------
# Task D: Filtering and Searching
# -------------------------------

print("\nAttendance > 90")
print(df[df["Attendance"] > 90])

print("\nTotal Marks > 90")
print(df[df["TotalMarks"] > 90])

print("\nFemale Students")
print(df[df["Gender"] == "F"])

print("\nMale Students")
print(df[df["Gender"] == "M"])

print("\nExternal Marks < 50")
print(df[df["ExternalMarks"] < 50])

# -------------------------------
# Task E: Ranking and Comparison
# -------------------------------

print("\nHighest Total Marks Student")
print(df.loc[df["TotalMarks"].idxmax()])

print("\nLowest Total Marks Student")
print(df.loc[df["TotalMarks"].idxmin()])

print("\nTop Three Performers")
print(df.nlargest(3, "TotalMarks"))

print("\nBottom Three Performers")
print(df.nsmallest(3, "TotalMarks"))

class_average = df["TotalMarks"].mean()

print("\nStudents Above Class Average")
print((df["TotalMarks"] > class_average).sum())

# -------------------------------
# Task F: Group-wise Analysis
# -------------------------------

print("\nAverage Total Marks of Male Students")
print(df[df["Gender"] == "M"]["TotalMarks"].mean())

print("\nAverage Total Marks of Female Students")
print(df[df["Gender"] == "F"]["TotalMarks"].mean())

print("\nAverage Attendance by Gender")
print(df.groupby("Gender")["Attendance"].mean())

# -------------------------------
# Task G: Data Visualization
# -------------------------------

# Bar Chart
plt.figure(figsize=(8,5))
plt.bar(df["Name"], df["TotalMarks"])
plt.title("Total Marks of Students")
plt.xlabel("Student Name")
plt.ylabel("Total Marks")
plt.show()

# Histogram
plt.figure(figsize=(6,5))
plt.hist(df["Attendance"], bins=5)
plt.title("Attendance Distribution")
plt.xlabel("Attendance")
plt.ylabel("Frequency")
plt.show()

# Pie Chart
gender_count = df["Gender"].value_counts()

plt.figure(figsize=(5,5))
plt.pie(gender_count,
        labels=gender_count.index,
        autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.show()

# Scatter Plot
plt.figure(figsize=(6,5))
plt.scatter(df["Attendance"], df["TotalMarks"])
plt.title("Attendance vs Total Marks")
plt.xlabel("Attendance")
plt.ylabel("Total Marks")
plt.show()

print("\nInterpretation:")
print("Students with higher attendance generally tend to have higher total marks.")

# -------------------------------
# Task H: Observations
# -------------------------------

print("\nOBSERVATIONS")
print("1. Female students have slightly higher average marks than male students.")
print("2. Students with attendance above 90% generally score better.")
print("3. Higher attendance appears to be associated with better academic performance.")
