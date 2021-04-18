# task 1
# Write a Python function, which Implements the Euler function.

def gcd(a, b):
	while a != 0 and b != 0:
		if a > b:
			a = a % b
		else:
			b = b % a
	return a+b

def mut_simple(n):
	count = 0
	for num in range(n+1):
		if gcd(num, n) == 1:
			count += 1
	return count

print(mut_simple(6))



# task 2
# Given a ticket number n, determine if it's lucky or not.
def is_lucky(number):
	length = len(str(number))
	left = 0
	right = 0
	if length % 2 == 0:
		for i in range(length//2):
			left += int(number[i])
			right += int(number[-i-1])
		if left == right:
			return True
		else:
			return False
	else:
		return "Not valid ticket number"


ticket = input("Your ticket number: ")
print(is_lucky(ticket))


# task 3
# Robot



# task 4 
# Write a python function, which returns the sum of digits of given number N

def digits_sum(num):
	result = 0
	for digit in num:
		result += int(digit)
	return result

number = input("Enter a number: ")
print(digits_sum(number))


# task 5
# Write a python program to find the next smallest palindrome of a specified number.
def is_palindrome(num):
	num = str(num)
	if num == num[::-1]:
		return True
	else:
		return False


def next_palindrome(number):
	while not is_palindrome(number):
		number+=1
	return number


number = int(input("Enter a number: "))
print(next_palindrome(number))