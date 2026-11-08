import matplotlib.pyplot as plt

students = ["Abin","John","Roy","Thomas","Shelby"]
marks = [12,35,65,45,33]

# BAR GRAPH
# plt.bar(students,marks)
# plt.title("Bar Chart")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.show()

# BAR GRAPH
# plt.boxplot(marks)
# plt.title("BOX Chart")
# plt.show()

# SCTEER

# plt.scatter(students,marks,s=[100,200,300,400,110])
# plt.title("Scatter Chart")
# plt.show()

# LINE
# plt.plot(students,marks,marker='o')
# plt.title("Line Chart")
# plt.show()

# HISTOGRAM
# plt.hist(marks, bins=5, edgecolor='black')
# plt.title("Histo Chart")
# plt.show()

# PIE CHART

plt.pie(marks,labels=students,autopct="%1.1f%%")
plt.show()