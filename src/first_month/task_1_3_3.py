# task 1
# Write a Python function which returns factorial value of given number n.

def fact(num):
	total = 1
	for number in range(1, num+1):
		total *= number
	return total


inp_num = int(input("input a number: "))

print(fact(inp_num))


# task 2
# Write a Python function which returns the n-th element of the fibonacci series.

def fib(n):
	