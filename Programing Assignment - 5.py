#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. Write a Python Program to Find LCM?
f_num = int(input("Enter the first number: "))
s_num = int(input("Enter the second number: "))
for i in range(1,f_num*s_num):
    if (i%f_num==0 and i%s_num == 0):
        print(f"LCM {i} is first num {f_num} and second number {s_num}.")


# In[ ]:


#2. Write a Python Program to Find HCF?
f_num = int(input("Enter the first number: "))
s_num = int(input("Enter the second number: "))
for i in range(1,f_num*s_num):
    if (i%f_num==0 and i%s_num == 0):
        H = (f_num*s_num)/i
        print(f"HCM {H} is first num {f_num} and second number {s_num}.")


# In[ ]:


#3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
a = 32            # decimal 
binary = bin(a)
print(f"Decimal {a} to binary conversion-->",binary)
octal = oct(a)
print(f"Decimal {a} to octal conversion-->",octal)
hexa = hex(a)
print(f"Decimal {a} to Hexadecimal conversion-->",hexa)


# In[ ]:


#4. Write a Python Program To Find ASCII value of a character?
character = input("Enter your fav character: ")
Ascii_value = ord(character)
print(f"ASCII Value {Ascii_value} of Character {character}.")


# In[ ]:


#5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?
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

