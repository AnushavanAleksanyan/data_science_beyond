# task 1
# Write a python program which returns a given list without duplicates.


def no_duplicates(lst):
	lst = list(set(lst))
	return lst

lst1 = [1, 5, 7, 8, 5, 12, 2, 9, 7]
print(no_duplicates(lst1))


# task 2
# Write a python program which returns common elements of 2 lists.

def commons(lst1, lst2):
	lst1 = set(lst1)
	lst2 = set(lst2)
	return lst1 & lst2

l1 = [1, 5, 7, 8, 3, 12, 2, 9, 7]
l2 = [8, 15, 17, 8, 5, 22, 7]
print(commons(l1,l2))


# task 3
# Write a python program which return elements which are in first list but not in second

def dif(lst1, lst2):
	lst1 = set(lst1)
	lst2 = set(lst2)
	lst = lst1 - lst2
	return lst


l1 = [1, 5, 7, 8, 3, 12, 2, 9, 7]
l2 = [8, 15, 17, 8, 5, 22, 7]
print(dif(l1,l2))


# task 4
# Write a python program which return elements are or in first list, either in second, but not in both

def unic(lst1, lst2):
	lst1 = set(lst1)
	lst2 = set(lst2)
	result = lst1 ^ lst2
	return result

l1 = [1, 5, 7, 8, 3, 12, 2, 9, 7]
l2 = [8, 15, 17, 8, 5, 22, 7]
print(unic(l1,l2))