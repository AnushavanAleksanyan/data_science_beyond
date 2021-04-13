# task 1
# Given two whole numbers - the lengths of the legs of a right-angled triangle - output its area.

side_a = 5
side_b = 4

area = side_a*side_b/2

print("area =", area)


# task 2
# Input a natural number n and output its last digit

# number = input("input a nutural number: ")

# last_digit = int(number)%10

# print(last_digit)


number = input("input a nutural number: ")

last_digit = number[-1]

print(last_digit)

# task 3
# Input a two-digit natural number and output the sum of its digits.

num = input("input a two-digit natural number: ")

# digits_sum = int(num)//10 + int(num)%10

# print(digits_sum)

digits_sum = int(num[0]) + int(num[1])

print(digits_sum)


# task 4
# You are given the first and second number in an arithmetic progression and natural number  n. Find n-th element of arithmetic progression.

first = 5
second  = 10
n = 4

n_th = first + (second - first) * (n-1)

print(n_th)