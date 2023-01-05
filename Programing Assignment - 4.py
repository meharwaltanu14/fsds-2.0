#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python Program to Find the Factorial of a Number?
n = int(input("enter the number: "))
fact = 1
for i in range(n):
    fact = fact*(n-i)
print(fact)


# In[ ]:


#2. Write a Python Program to Display the multiplication Table?
n = int(input("Enter the number of Table: "))
for i in range(1,11):
    print(f"{i} X {n} =",n*i)


# In[ ]:


#3. Write a Python Program to Print the Fibonacci sequence?
a = 0 
b = 1
n = int(input("How many number you want in fibonacci sequence: "))
for i in range(n):
    c = a+b
    a = b
    b = c
    print(c)    


# In[ ]:


#4. Write a Python Program to Check Armstrong Number?
num = int(input("Enter a number: "))
sum = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if num == sum:
    print(num,"is an Armstrong number")
else:
    print(num,"is not an Armstrong number")


# In[ ]:


#5. Write a Python Program to Find Armstrong Number in an Interval?
x=int(input("lower limit: "))
y=int(input("upper limit: "))
print("Armstrong Numbers are: ")
for Number in range(x,y):
    digits=0
    temp=Number
    while temp>0: 
        digits=digits+1
        temp=temp//10
        sum=0
        temp=Number
        while temp>0: 
            last_digit=temp%10
            sum=sum+(last_digit**digits)
            temp=temp//10
    if Number == sum:
        print(Number)


# In[ ]:


#6. Write a Python Program to Find the Sum of Natural Numbers?
n = int(input("Enter the number: "))
sum = 0
for i in range(1,n+1):
    sum = sum + i
print(sum)    


# In[ ]:




