# task 1
# Write a python program, which adds a new value with the given key in dict.

def add_val(key, val, dict):
	dict[key] = val
	return dict

d = {}
print(add_val("Key","Value", d))


# task 2
# Write a python program which concat 2 dicts.

# def concat_dicts(dict1, dict2):
# 	for item in dict2.items():
# 		dict1.update(item)
# 	return dict1

d1 = {1:"one", 2:"two"}
d2 = {3:"there", 4:"four", 5:"five"}
for item in d2.items():
	d1.update(item)
print(d1)
# print(concat_dicts(d1, d2))


# task 3
# Write a python program, which create a dictionary for given number N, where keys are numbers from 1 to N, and values are cubs of that numbers


# task 4
# Write a python program which create dict from 2 lists with the same length


# task 5
# Write a python program which gets the maximum and minimum values of a dictionary.


# task 6
# Write a python program which combines 2 dictionaries into one, if there is an element with the same key, appropriate element of combined dict will be an element with that key, and sum of values as value.


# task 7
# Write a python program which create dict from string, where keys are letters of  string, values are counts of letters in string
