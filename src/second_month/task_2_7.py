import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# task_2_7_1
# Write a Python program to draw a line with suitable label in the x axis, y axis and a title.
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
data = np.sin(np.arange(60))
print(data)
ax.plot(data)
ax.set_xticks([10,20,30,40,50])
ax.set_yticks([-2,-1,0,1,2])
ax.set_xticklabels(['one', "two", "three", "four", "five"], rotation=45, size = 9)
ax.set_xlabel("values")
ax.set_title("sinusoid")
# plt.show()


# task_2_7_2
# Write a Python program to draw line charts of the financial data of Alphabet Inc. 
# between October 3, 2016 to October 7, 2016
data = pd.read_csv("other/task-2-7/task_2_7_2.csv", header = None, index_col = 0)
print(data)
print(data.iloc[1])

data.plot(marker='o')
plt.show()