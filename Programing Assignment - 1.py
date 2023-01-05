#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program to print "Hello Python"
print("Hello Python")


# In[ ]:


#2. Write a Python program to do arithmetical operations addition and division.?
print('Select a Arithmetic Operation:         \n1.Addition(+)        \n2.Division(-)        \n2.Multiplication(*)        \n4.Division(/)        \n3.Stop(0)\n')
first_num = int(input("Enter the first number: "))
sec_num = int(input("Enter the second number: "))
operator = input("Enter the operator: ")
if (operator == '+' or operator == '-' or operator == '*' or operator == '/'):
    print("Valid Input")
    if (operator == '+' ):
        print(f"Sum of first number {first_num} and second number {sec_num} is",first_num+sec_num)
    elif (operator == '-' ):
        print(f"Difference of first number {first_num} and second number {sec_num} is",first_num-sec_num)
    elif (operator == '*' ):
        print(f"Multiply of first number {first_num} and second number {sec_num} is",first_num*sec_num)
    elif (operator == '/' ):
        print(f"Division of first number {first_num} and second number {sec_num} is",first_num/sec_num)
    elif (operator == '0'): 
        print("Stop")
else:
    print("Invalid Input\nPlease Enter valid operator (*,+,-,/)")


# In[ ]:


#3. Write a Python program to find the area of a triangle?
l = eval(input("Enter the length of Triangle: "))
b = eval(input("Enter the breath of Triangle: "))
area_triangle = 0.5*l*b
print(round(area_triangle))


# In[ ]:


#4. Write a Python program to swap two variables?
a = input("Enter the first value: ")
b = input("Enter the second value: ")
c = a
a = b
b = c
print(f"after swaping first value {a}\nSecond value {b}")
a,b = b,a
print(f"after swaping first value {a}\nSecond value {b}")


# In[ ]:


#5. Write a Python program to generate a random number?
import random           # import random module
from random import randint 
# randint(start value, end value) 
randint(4,7)# here randomly generate number 

