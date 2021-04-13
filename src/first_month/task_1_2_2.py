# task 1
# Write a Python program to multiply all the items in a list.

lst = [2, 5, 6, 8, 1, 12, 4]
result= 1
for elem in lst:
	result *= elem

print(result)


# task 2
# Write a Python program to get the largest number from a list.

lst = [2, 5, 6, 8, 1, 12, 4]

largest = 0

for elem in lst:
	if elem > largest:
		largest = elem

print(largest)


# task 3
# Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)
lst = [a**2 for a in range(1,31)]

print(lst[5:])


# task 4
# Write a Python program to remove duplicates from a list


lst = [2, 5, 12, 4, 6, 2, 8, 4, 1, 12, 4]

print(list(set(lst)))


# task 5
# Write a Python program to find the most appeared element in a list.

lst = [2, 5, 12, 2, 6, 2, 8, 4, 1, 12, 4]

most_appeared = 0
count = 0
for elem in lst:
	if lst.count(elem)>count:
		count = lst.count(elem)
		most_appeared = elem

print(most_appeared, "is the most appeared element in the list. It appeared", count, "times.")