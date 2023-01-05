#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python Program to Check if a Number is Positive, Negative or Zero?
num = int(input("enter the number: "))
if num>0:
    print(f"Given number {num} is positive.")
elif num<0:
    print(f"Given number {num} is negative.")
else:
    print(f"Given number {num} is Zero")


# In[ ]:


#2. Write a Python Program to Check if a Number is Odd or Even?
num = int(input("Enter the number: "))
if num%2==0:
    print(f"Given number {num} is even.")
else:
    print(f"Given number {num} is odd.")


# In[ ]:


#3. Write a Python Program to Check Leap Year?
year = int(input("enetr number of year :"))
if year%400==0:
    print("given year is a leap year")
elif year%100!=0 and year%4==0:
    print("given year is a leap year")
else:
    print("given year is not a leap year")


# In[ ]:


#4. Write a Python Program to Check Prime Number?
n = int(input("enter the number: "))
if (n<2:
    print(f"Given number {n} is not prime.")
else:    
    for i in range(2,n):
        if n%i==0:
            print(f"Given number {n} is not prime.")
            break
        else:
            print(f"Given number {n} is prime.")
            break


# In[ ]:


#5. Write a Python Program to Print all Prime Numbers in an Interval of 1-10000?
l1 = []
for x in range(1,10000):
    flag=False
    for y in range(2,x):
        if (x%y ==0):
            flag = True
            break
    if (not flag):
        l1.append(x)
print(l1)        


# In[ ]:




