# task 1
# Write a Python program to get the largest number from a list.

lst = [2, 75, 25, 8, 19 , 12, 45]
lst.sort()

print(lst[-1])


# task 2
# Write a Python program to get the frequency of the given element in a list to.
elem = 5
lst = [2, 75, 5, 25, 8, 19, 5, 12, 5, 45]

print(lst.count(elem))


# task 3
# Write a Python program to remove the second element from a given list, if we know that the first elements index with that value is n. 

val_to_remove = 5
lst = [2, 75, 5, 25, 8, 19, 5, 12, 5, 45]
frst_elem_indx = 2
idx = lst.index(val_to_remove, frst_elem_indx+1)  #find second element index
lst.pop(idx)

print(lst)