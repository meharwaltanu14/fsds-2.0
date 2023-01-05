#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python program to convert kilometers to miles?
k_m  = eval(input("Enter the ditance in Kilometer unit: "))
miles = k_m* 0.621371192237
print(f"{k_m}km = {round(miles,2)}miles")


# In[ ]:


#2. Write a Python program to convert Celsius to Fahrenheit?
cel = eval(input("enter the temprature in celsius: "))
fah = (cel*9/5)+32
print(f"{cel} degree celsius = {fah} degree farenheit")


# In[ ]:


#3. Write a Python program to display calendar?
import calendar      # we import the calendar module 
year = int(input("Enter the year: "))
print(calendar.calendar(year)) 


# In[ ]:


#4. Write a Python program to solve quadratic equation?
import math
import cmath
a = int(input("enter a value: "))
b = int(input("enter b value: "))
c = int(input("enter c value: "))
d = math.pow(b,2)-4*a*c
if d==0:
    r1 = -b/2*a
    r2 = -b/2*a
    print("roots are same",r1,r2)
elif d > 0:
    r1 = (-b-cmath.sqrt(d))/(2 * a)
    r2 = (-b+cmath.sqrt(d))/(2 * a)
    print("roots are Real and different",r1,r2)   
else:
    r1 = (-b-cmath.sqrt(d))/(2 * a)
    r2 = (-b+cmath.sqrt(d))/(2 * a)
    print("roots are imagnery",r1,r2)


# In[ ]:


#5. Write a Python program to swap two variables without temp variable?
num1 = int(input("enter the first value: "))
num2 = int(input("enter the second value: "))
num1 = num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print(f"after swaping first value {num1} and second value {num2}.")


# In[ ]:




