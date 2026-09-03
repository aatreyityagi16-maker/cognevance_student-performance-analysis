import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('student_performance_dataset.csv')

subjects = ['Math_Marks', 'Science_Marks', 'English_Marks']
df["Average_Marks"] = df[subjects].mean(axis=1)

print("Average marks by subject:")
print(df[subjects].mean().round(2))

print("\nCorrelation between attendance and average marks:")
print(round(df["Attendance_Percent"].corr(df["Average_Marks"]), 3))

# Bar chart
df[subjects].mean().plot(kind="bar", title="Average Marks by Subject")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig("average_marks_by_subject.png")
plt.show()

# Histogram
plt.figure()
plt.hist(df["Average_Marks"], bins=6)
plt.title("Distribution of Average Marks")
plt.xlabel("Average Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig("average_marks_histogram.png")
plt.show()

# Pie chart
counts = df["Performance"].value_counts()
plt.figure()
plt.pie(counts, labels=counts.index, autopct="%1.1f%%")
plt.title("Student Performance Categories")
plt.tight_layout()
plt.savefig("performance_categories_pie.png")
plt.show()

# Attendance relationship
plt.figure()
plt.scatter(df["Attendance_Percent"], df["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.tight_layout()
plt.savefig("attendance_vs_marks.png")
plt.show()
