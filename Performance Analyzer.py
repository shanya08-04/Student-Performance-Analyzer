import pandas as pd
import matplotlib.pyplot as plt

#you can add or remove student data use csv file (attached with file)


df = pd.read_csv("students.csv")

# Calculate total and average
df["Total"] = df.iloc[:, 1:].sum(axis=1)
df["Average"] = df["Total"] / 5

print("\nStudent Performance Summary:\n")
print(df[["Name", "Total", "Average"]])
topper = df.loc[df["Total"].idxmax()]
print("-------------------------------------------")
print("\nTop Performer:")
print(topper["Name"], "-", topper["Total"])
print("-------------------------------------------")

# --------------
plt.figure()
plt.bar(df["Name"], df["Average"])
plt.title("Average Marks of Students")
plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# ---------------
subject_avg = df.iloc[:, 1:6].mean()

plt.figure()
subject_avg.plot(kind="bar")
plt.title("Subject-wise Average Marks")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.xticks(rotation=30)
plt.tight_layout()
plt.show()

# -------------
student_name = input("\nEnter student name for detailed graph: ")

student_data = df[df["Name"].str.lower() == student_name.lower()]

if not student_data.empty:
    marks = student_data.iloc[0, 1:6]

    plt.figure()
    marks.plot(kind="line", marker='o')
    plt.title(f"{student_name}'s Performance")
    plt.xlabel("Subjects")
    plt.ylabel("Marks")
    plt.grid()
    plt.show()
else:
    print("Student not found!")
