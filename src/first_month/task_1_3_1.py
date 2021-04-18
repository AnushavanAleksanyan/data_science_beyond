# task 1
# Write a Python function, which gets 2 numbers, and return True if the second number is first number divider, otherwise False.

def is_devider(a, b):
	if a % b == 0:
		return True
	else:
		return False

print(is_devider(10, 3))


# task 2
# Write a Python function, which gets a number, and return True if that number is palindrome, otherwise False

def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		print(True)
	else:
		print(False)

is_palindrome(454)


# task 3
# Write a Python function, which gets a number, and return True if that number is prime, otherwise False.

def is_prime(number):
	if isinstance(number, int):
		if number == 1:
			return False
		for i in range(2, int(number/2)+1):
			if number % i == 0:
				return False
		else:
			return True


inp_num = int(input("Input a number: "))
print(is_prime(inp_num))


# task 4
# Write a Python function, which checks if a number is perfect - that is equal to the sum of its proper positive divisors.

def is_perfects(nmbr):
	summ = 0
	for n in range(1, nmbr):
		if nmbr%n==0:
			summ +=n
	if summ == nmbr:
		return f"{nmbr} is perfect number"
	else:
		return f"{nmbr} is not perfect number"

inp_num = int(input("Input a number: "))
print(is_perfects(inp_num))


# task 5
# Write a function, which gets 2 numbers, and return their Great common divisor

def gcd(a, b):
	while a != 0 and b != 0:
		if a > b:
			a = a % b
		else:
			b = b % a
	return a+b

print(gcd(75,30))