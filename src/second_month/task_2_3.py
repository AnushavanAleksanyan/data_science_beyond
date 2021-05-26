import numpy as np
from numpy import newaxis


# task_2_3_1
# Write a NumPy program to find maximum and minimum values of an array
def min_max(arr):
	mx = np.max(arr)
	mn = np.min(arr)
	return mn, mx


# task_2_3_2
# Write a NumPy program to find maximum and minimum values of the secont column of an array
def min_max_second_col(arr):
	mx = np.max(arr[:,1])
	mn = np.min(arr[:,1])
	return mn, mx


# task_2_3_3
# Write a NumPy program to find median of an array
def mediana(arr):
	return np.median(arr)


# task_2_3_4
# Create one dimention and two dimention arrays and multiply them
def mult(arr1, arr2):
	return arr1[:,newaxis]*arr2

def main():
	arr = np.random.randint(2,20, size=(10,5))
	a = np.array([2, 5, 7, 4])
	b = np.array([[3, 2, 4],[1,2,5],[2,1,3],[4,1,5]])
	print(arr)
	print(arr[:,1])
	print(min_max(arr))                # task_2_3_1
	print(min_max_second_col(arr))     # task_2_3_2
	print(mediana(arr))                # task_2_3_3
	print(mult(a,b))                   # task_2_3_4


main()