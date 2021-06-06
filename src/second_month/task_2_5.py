import pandas as pd
import csv


# task_2_5_1
# Write a Pandas program to display all the records of REGIONS file
df = pd.read_csv('other/region.csv')
print(df)


# task_2_5_2
# Write a Pandas program to display all the location id from locations file.
df = pd.read_csv('other/location.csv')
print(df["LOCATION_ID"])


# task_2_5_3
# Write a Pandas program to extract first 7 records from employees file.
df = pd.read_csv('other/employees.csv')
print(df.loc[:6])


# task_2_5_4
# Write a Pandas program to select distinct department id from employees file.
df = pd.read_csv('other/employees.csv')
print(df["DEPARTMENT_ID"])


# task_2_5_5
# Write a Pandas program to display the first, last name, salary and department number for those employees whose first name starts with the letter 'S'.
df = pd.read_csv('other/employees.csv')
colomns = ["FIRST_NAME","LAST_NAME","SALARY","DEPARTMENT_ID"]
print(df.loc[df["FIRST_NAME"].str.get(0)=="S", colomns])
