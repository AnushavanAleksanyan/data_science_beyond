import numpy as np

# task 2_1_1
# convert a list of numeric values into a one-dimensional NumPy array

def list_to_array(lst):
	return np.array(lst)


# task 2_1_2
# create a NumPy array with values ranging from 2 to 10

def create_array():
	arr = np.arange(2,11)
	return arr


# task 2_1_3
# create a null vector of size 10 and update sixth to eight values to 11

def zeroes():
	arr = np.zeros(10)
	for i in range(5,8):
		arr[i] = 11
	return arr

# task 2_1_4
# test whether each element of a 1-D array is also present in a second array.

def compare(arr1, arr2):
	for elem in arr1:
		if not elem in arr2:
			return "False"
	return "True"


l1 = [5,6,8]
print(list_to_array(l1))   # task 2_1_1

print(create_array())    # task 2_1_2

print(zeroes())   # test 2_1_3


l2 = np.array([5,6,8,7])
l3 = np.array([5,6,8,7,9,3])

print(compare(l2, l3))