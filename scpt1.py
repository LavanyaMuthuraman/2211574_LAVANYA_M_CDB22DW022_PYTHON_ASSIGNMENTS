# -*- coding: utf-8 -*-
"""scpt1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hd-Et7U1F46sz8dyX3cg2HBLf4GWGv35
"""

number=int(input('Enter the number:'))
for number in range(number+1):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            print(number)

n = int(input('Enter the number:'))
for i in range(1,n+1):
  if(isPrime(i)):
    print(i,end=" ")