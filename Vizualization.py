import matplotlib.pyplot as plt
students = ['A', 'B', 'C', 'D', 'E']
marks = [75, 85, 60, 90, 70]

# 1. Bar Chart
plt.subplot(2, 3, 1)

plt.bar(students, marks)
plt.title("Bar Chart")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

plt.boxplot(marks)
plt.title("Box Plot")
plt.show()

plt.scatter(students, marks, s=[100, 200, 150, 300, 120])
plt.title("Bubble Chart")
plt.show()

plt.plot(students, marks, marker='o')
plt.title("Line Chart")
plt.show()

plt.hist(marks, bins=5, edgecolor='black')
plt.title("Histogram")
plt.show()

plt.scatter(students, marks)
plt.title("Scatter Plot")
plt.show()

plt.pie(marks, labels=students, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()