import numpy as np
from numpy.linalg import inv, det

# task_2_2_1
# Write a NumPy program to compute the multiplication of two given matrixes
def mul(a1,a2):
	return a1.dot(a2)


# task_2_2_2
# Write a NumPy program to compute the determinant of an array
def determinant(arr):
	return det(arr)


# task_2_2_3
# Write a NumPy program to compute the sum of the diagonal element of a given array
def diag_sum(arr):
	return np.trace(arr)


# task_2_2_4
# Write a NumPy program to compute the inverse of a given matrix
def inverse(arr):
	return inv(arr)


# task_2_2_5
# Write a NumPy program to generate matrix and write it to a file, then again read from file that matrix.
def mat_to_file(low, hight):
	arr = np.random.randint(low, hight, size=(3, 6))
	np.save('file', arr)
	info = np.load('file.npy')
	print(info)


def main():
	arr1 = np.arange(1,12,3)
	arr2 = np.arange(10,2,-2)
	arr3 = np.array([[1, 2, 3],[7,8,9]])
	arr4 = np.array([[2,3, 1],[3,5, 5],[1,4, 8]])
	print(arr4[0])
	arr2[1:2]=55
	print(arr3.T)
	print(arr3.dot(arr4))
	print(mul(arr3,arr4))   # task.2.2.1

	print("determinant")    # task.2.2.2
	print(determinant(arr4))

	print(diag_sum(arr4))   # task.2.2.3

	print (inverse(arr4))   # task.2.2.4

	mat_to_file(2,6)        # task.2.2.5


main()