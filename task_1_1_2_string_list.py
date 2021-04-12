# STRINGS
# task 1
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given string.

string = "Some string"
output = string[:2] + string[-2:]

print(output)


# task 2
# Write a Python program to remove the nth index character from a nonempty string.

text = "Some text"
n = 3

result = text[:n-1] + text[n:]

print(result)


# task 3
# Write a Python program to change a given string to a new string where the first and last chars have been exchanged.

text = "Some text"
changed = text[-1]+text[1:-1]+text[0]

print(changed)


# task 4
# Write a Python function to get a string made of 4 copies of the last two characters of a specified string

def echo(text):
	return text[-2:]*4

string = "Hello"

print(echo(string))



# LISTS

# task 1
# Write a Python program that make a list from given string
text = "Good Bye"

print(list(text))

# task 2
# Write a Python program to print a new list which is the equivalent given list after removing the 0th, 4th and 5th elements.

lst = [7, 5, 12, 6, 4, 11, 27]
new_lst = lst[1:4]+lst[6:]

print(new_lst)


# task 3
# Write a Python program which add an element to the given list

lst = [7, 5, 12, 6, 4, 11, 27]
value = 22
lst.append(value)
print(lst)


# task 4
# Write a Python program which concat 2 lists.

lst_1 = [17, 35, 12, 26, 4, 19, 23]
lst_2 = [5, 14, 88, 8, 4, 16, 3]
lst_1.extend(lst_2)

print(lst_1)