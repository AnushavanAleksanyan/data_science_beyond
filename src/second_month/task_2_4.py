import pandas as pd
import numpy as np


# task_2_4_1
# Write a Pandas program to add, subtract, multiple and divide two Pandas Series
def add_series(s1, s2):
	return s1.add(s2, fill_value=0)

def sub_series(s1, s2):
	return s1.sub(s2, fill_value=0)

def mul_series(s1, s2):
	return s1.mul(s2, fill_value=0)

def div_series(s1, s2):
	return s1.div(s2, fill_value=0)


# task_2_4_2
# Write a Pandas program to convert a dictionary to a Pandas series.
def dict_to_series(dict):
	return pd.Series(dict)


# task_2_4_3
# Write a Pandas program to convert a NumPy array to a Pandas series
def array_to_series(arr):
	return pd.Series(arr)


# task_2_4_4
# Write a Pandas program to convert the first column of a DataFrame as a Series
def dfcol_to_series(df):
	return pd.Series(df.iloc[:,0])


# task_2_4_5
# Write a Pandas program to sort a given Series
def sort_series(ser):
	return ser.sort_values()


# task_2_4_6
# Write a Pandas program to select the rows the score is between 15 and 20 (inclusive).
def sliced(ser):
	return ser.iloc[:][ser[0]<=25][ser[0]>=15]


# task_2_4_7
# Write a Pandas program to calculate the sum of the examination attempts by the students.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
			'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
			'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
			'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

df = pd.DataFrame(exam_data, index=labels)
print(sum(df['attempts']))



def main():
	# task_2_4_1
	a = [1, 7, 2]
	b = [2, 6, 3]
	a1 = pd.Series(a, index = ["x", "y", "z"])
	a2 = pd.Series(b, index = ["z", "x", "d"])
	print(add_series(a1,a2))
	print(sub_series(a1,a2))
	print(mul_series(a1,a2))
	print(div_series(a1,a2))

	# task_2_4_2
	d1 = {
		"A": [1,5,6],
		"B": 6,
		"C": 5,
	}
	print(dict_to_series(d1))

	# task_2_4_3
	a = np.arange(2,15,3)
	print(array_to_series(a))

	# task_2_4_4
	data = {
	"name":["Mike", "Jack", "Joe"],
	"age":[22,35,14]
	}
	dataf = pd.DataFrame(data)
	print(dataf)
	print(dfcol_to_series(dataf))

	# task_2_4_5
	print(sort_series(dfcol_to_series(dataf)))

	# task_2_4_6
	data = pd.DataFrame(np.arange(100).reshape(20,5))
	print(sliced(data))

	# task_2_4_7


main()