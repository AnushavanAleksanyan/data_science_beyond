import pandas as pd
import numpy as np


# task_2_6_1
# Write a Pandas program to split the following dataframe into groups based on school code
df = pd.read_csv("other/task-2-6/school.csv")
def group_by_school(dataf):
	gb = dataf.groupby('school')
	for key, value in gb:
		print(gb.get_group(key))



# task_2_6_2
# Write a Pandas program to split the following given dataframe by school code and get mean, min, and max value of age for each school
def mean_min_max(dataf):
	mean = dataf.groupby("school")['age'].mean().reset_index(name="mean")
	min = dataf.groupby("school")['age'].min().reset_index(name="min")
	max = dataf.groupby("school")['age'].max().reset_index(name="max")
	print(pd.concat([mean, min, max], axis=1))


# task_2_6_3
# Write a Pandas program to split the following given dataframe into groups based on school code and class
def group_by_school_class(dataf):
	grouped = dataf.groupby(["school", "class"])
	for key, value in grouped:
		print(grouped.get_group(key))

# task_2_6_4
# Write a Pandas program to split the following given dataframe into groups based on school code
# and cast grouping as a list
def group_by_school_list(dataf):
	print(type(dataf))
	print(dataf.groupby("school").agg(list))


# task_2_6_5
# Write a Pandas program to split a dataset, group by one column and get mean, min, and max values by group.
# Using the following dataset find the mean, min, and max values of purchase amount (purch_amt) group by customer id (customer_id)
df2 = pd.read_csv("other/task-2-6/restourant.csv")
def mean_min_max_rest(dataf, col, by_col):
	mean = dataf.groupby(col)[by_col].mean()
	min = dataf.groupby(col)[by_col].min()
	max = dataf.groupby(col)[by_col].max()
	print(pd.concat([mean, min, max], axis=1))


def main():
	print("<task2_6_1>")
	group_by_school(df)  # task2_6_1
	print("\n<task2_6_2>")
	mean_min_max(df)     # task2_6_2
	print("\n<task2_6_3>")
	group_by_school_class(df)   # task2_6_3
	print("\n<task2_6_4>")
	group_by_school_list(df)     # task2_6_4
	print("\n<task2_6_5>")
	mean_min_max_rest(df2, "customer_id", "purch_amt")     # task2_6_5



main()