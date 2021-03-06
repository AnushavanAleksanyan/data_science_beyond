# task 1
# Write a python program, which adds a new value with the given key in dict.

def add_val(key, val, dict):
	dict[key] = val
	return dict

d = {}
print(add_val("Key","Value", d))


# task 2
# Write a python program which concat 2 dicts.

def concat_dicts(dict1, dict2):
	dict1.update(dict2)
	return dict1

d1 = {1:"one", 2:"two"}
d2 = {3:"there", 4:"four", 5:"five"}

print(concat_dicts(d1,d2))



# task 3
# Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers

def cubes(number):
	dict = {}
	for key in range(1, number+1):
		dict[key] = key**3
	return dict

print(cubes(5))



# task 4
# Write a python program which create dict from 2 lists with the same length

def combine(lst1, lst2):
	dict = {}
	for i in range(len(lst1)):
		dict[lst1[i]]=lst2[i]
	return dict

l1 = [1, 2, 3, 4, 5, 6]
l2 = ["one", "two", " there", "four", "five", "six"]

print(combine(l1, l2))

# task 5
# Write a python program which gets the maximum and minimum values of a dictionary.


def min_max(dict):
	m = list(dict.values())
	m.sort()
	return m[0], m[-1]

d = {1:"one", 2:"two", 5:"five", 10:"ten"}
print(min_max(d))

# task 6
# Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.

def comb2(dict1,dict2):
	for key in dict2.keys():
		if key in dict1.keys():
			dict1[key] +=dict2[key]
		else:
			dict1[key] =dict2[key]
	return dict1


d1 = {"a":1, "b":2, "c":3}
d2 = {"e":11, "c":8, "d":5}
print(comb2(d1,d2))

# task 7
# Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string

def newdict(text):
	d = {}
	for let in text:
		d[let] = text.count(let)
	return d


t = "All string methods returns new values. They do not change the original string."

print(newdict(t))