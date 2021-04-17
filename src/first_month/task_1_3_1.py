# task 1
# Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.

def is_devider(a, b):
	if a % b == 0:
		return True
	else:
		return False

print(is_devider(10, 3))