# task 1
# Write a Python function which returns factorial value of given number n.

def fact(num):
	if num ==1:
		return 1
	return num * fact(num-1)


inp_num = int(input("input a number: "))

print(fact(inp_num))


# task 2
# Write a Python function which returns the n-th element of the fibonacci series.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 .....


def fib(n):
	if n < 2:
		return n
	return fib(n-2)+fib(n-1)

print(fib(7))