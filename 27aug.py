# exception Exception - event occurring during execution of program that disrupts normal flow of program . these are the situations in which pyhton interpreter cant handle

#WHY IT IS DANGEROUS- 
#1.leads to sudden termination of programs
#2. can block the applications
#3. data loss can occur
#4.corrupt data files.

#EXCEPTION VS ERROR-
#ERROR cannot be handled 
#	can be handled using exception handling syntax
#4 blocks provide in exception handling in python:
#write , except, else, find block

# x=int(input("enter a no 1"))
# y= int(input("enter a no 2"))
# div= x/y
# print(div)
#it will show zero division error if y=0 because we cant divide by 0. so we can handle this using exception handling syntax

# x=int(input("enter a no 1:"))
# y= int(input("enter a no 2:"))
# try:
#     div= x/y
#     print(div)
# except (ZeroDivisionError, NameError):
#     print("Error: Division by zero is not allowed.")

# explain basic structure of python program with example
# data types with syntax and example
# 3. explain python variables, constants and identifiers with rules and example 
# discuss type conversion , explicit and implicit conversion
# all operators of python
# precedence and associativity with example
# conditional statements all
# looping statement for and while
# break, continue and pass statement
# different function arguments in python
# python function in detail, define , calling and return value with example.