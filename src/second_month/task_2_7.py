import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# task_2_7_1
# Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(3,2,1)
data = np.sin(np.arange(60))
ax.plot(data)
ax.set_xticks([10,20,30,40,50])
ax.set_yticks([-2,-1,0,1,2])
ax.set_xticklabels(['one', "two", "three", "four", "five"], rotation=-45, size = 9)
ax.set_xlabel("values")
ax.set_title("sinusoid")


# task_2_7_2
# Write a Python program to draw line charts of the financial data of Alphabet Inc.
# between October 3, 2016 to October 7, 2016
data2 = pd.read_csv("other/task-2-7/task_2_7_2.csv", header = None, index_col = 0)
bx = fig.add_subplot(3,2,2)
bx.plot(data2,marker='o')
bx.tick_params(axis = "x", labelrotation=45)


# task_2_7_3
# Write a Python program to display the grid and draw line charts of the closing value of
# Alphabet Inc. between October 3, 2016 to October 7, 2016.
# Customized the grid lines with linestyle -, width .5. and color blue.
data3 = pd.read_csv("other/task-2-7/task_2_7_3.csv", header = None, index_col = 0)
cx = fig.add_subplot(3,2,3)
cx.plot(data3, marker='*')
cx.tick_params(axis = "x", labelrotation=45)
cx.grid(lw=0.5, color="blue")

# task_2_7_4
# Write a Python programming to display a bar chart of the popularity of programming Languages
data4 = {"Programming languages": ["Java", "Python", "PHP", "JavaScript", "C#", "C++"],
		"Popularity": [22.2, 17.6, 8.8, 8, 7.7, 6.7]}
dx = pd.DataFrame.from_dict(data4)
dx = fig.add_subplot(3,2,4)
dx.bar(data4["Programming languages"], data4["Popularity"])
dx.tick_params(axis = "x", labelrotation=45)


# task_2_7_5
# Write a Python programming to create a pie chart of the popularity of programming Languages.
data5 = data4
ex = pd.DataFrame.from_dict(data5)
ex = fig.add_subplot(3,2,5)
explode = (0, 0.1, 0, 0, 0, 0)
ex.pie(data5["Popularity"], labels = data4["Programming languages"], explode = explode, shadow = True)




# task_2_7_6
# Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.









plt.tight_layout(pad=0.4, w_pad=2, h_pad=3)
plt.show()