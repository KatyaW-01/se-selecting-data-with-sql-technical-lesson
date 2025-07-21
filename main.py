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

employees_by_role = pd.read_sql("""
SELECT firstName, lastName, jobTitle,
    CASE
    WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
    ELSE "Not Sales Rep"
    End AS role
  FROM employees;
""", conn).head(10)

print(employees_by_role)

employees_with_location = pd.read_sql("""
SELECT firstName, lastName, officeCode,
    CASE
    WHEN officeCode = "1" THEN "San Francisco, CA"
    WHEN officeCOde = "2" THEN "Boston, MA"
    WHEN officeCode = "3" THEN "New York, NY"
    WHEN officeCode = "4" THEN "Paris, France"
    WHEN officeCode = "5" THEN "Tokyo, Japan"
    END AS office
  FROM employees;               
""", conn).head(10)

print(employees_with_location)

#Shorter syntax when just checking if a value is equal to another value (in this case, repeating officeCode = )
employees_with_location = pd.read_sql("""
SELECT firstName, lastName, officeCode,
       CASE officeCode
       WHEN "1" THEN "San Francisco, CA"
       WHEN "2" THEN "Boston, MA"
       WHEN "3" THEN "New York, NY"
       WHEN "4" THEN "Paris, France"
       WHEN "5" THEN "Tokyo, Japan"
       END AS office
  FROM employees;
""", conn).head(10)

#SQL build in functions

#length
employee_name_lengths = pd.read_sql("""
SELECT length(firstName) AS name_length
  FROM employees;
""", conn).head()

print(employee_name_lengths)

#upper (change to uppercase)
upper_employees = pd.read_sql("""
SELECT upper(firstName) AS name_in_all_caps
  FROM employees;
""", conn).head()

print(upper_employees)

#substr (string slicing)
employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) AS first_initial
  FROM employees;
""", conn).head()

print(employees_initials)

#same thing but adding a . after each first initial
employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) || "." AS first_initial
  FROM employees;
""", conn).head()

print(employees_initials)

#concatenate first and last names with a space in between 
employees_full_names = pd.read_sql("""
SELECT firstName || " " || lastName AS full_name
  FROM employees;
""", conn).head()

print(employees_full_names)


#functions for math operations 
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print(order_details)

#round
rounded_prices = pd.read_sql("""
SELECT round(priceEach) AS rounded_price
  FROM orderDetails;
""", conn)

print(rounded_prices)

#CAST (can use to return integers instead of floating point numbers)
rounded_prices = pd.read_sql("""
SELECT CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails;
""", conn)

print(rounded_prices)

#basic math operations
totals = pd.read_sql("""
SELECT priceEach * quantityOrdered AS total_price
  FROM orderDetails;
""", conn)

print(totals)


#date and time operations
orders = pd.read_sql("""SELECT * FROM orders;""", conn)
print(orders)

#how many days remaining between requiredDate and orderDate
days_remaining = pd.read_sql("""
SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
  FROM orders;
""", conn)

print(days_remaining)

#strftime function
order_dates = pd.read_sql("""
SELECT orderDate,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year,
       strftime("%d", orderDate) AS day
  FROM orders;
""", conn)

print(order_dates)

conn.close()
                                      