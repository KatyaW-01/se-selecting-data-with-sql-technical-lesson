import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

employee_data = pd.read_sql("""SELECT * FROM employees;""", conn)
#print(employee_data)

employee_first_and_last = pd.read_sql(""" 
SELECT lastName, firstName
  FROM employees;
""", conn).head()

print(employee_first_and_last)

#use AS keyword to change the column name in the query result
employees_first_names = pd.read_sql("""
SELECT firstName AS name
  FROM employees;
""", conn).head()
print(employees_first_names)
                                      