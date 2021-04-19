# task 1
# Write a Python function which returns factorial value of given number n.

def fact(num):
	if num ==1:
		return 1
	return num * fact(num-1)


inp_num = int(input("input a number: "))

print(fact(inp_num))


# task 1-2
# factorial with loop

def factor(num):
	total = 1
	for number in range(1, num+1):
		total *= number
	return total


inp_num = int(input("input a number: "))

print(factor(inp_num))


# task 2
# Write a Python function which returns the n-th element of the fibonacci series.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 .....


def fib(n):
	if n ==1:
		return 0
	elif n == 2:
		return 1
	return fib(n-2)+fib(n-1)

print(fib(1))


# task 2-2
# fibonacci with loop


def fibon(m):
	frst = 0
	scnd = 1
	res = 0
	if m == 1:
		return frst
	elif m == 2:
		return scnd
	else:
		for num in range(2,m):
			res = frst + scnd
			frst = scnd
			scnd = res
		return res


print(fibon(9))