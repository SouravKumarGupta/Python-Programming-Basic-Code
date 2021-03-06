# -*- coding: utf-8 -*-
"""
Created on Tue Jan  4 12:05:53 2022

@author: User
"""
# Question 1:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

import math
def calculates_given_formula():
  C=50
  H=30
  inp=input("Enter value of D: ")
  d=inp.split(",")
  res=[]
  for D in d:
    Q = math.sqrt((2 * C * int(D))/H)
    res.append(round(Q))
  return res

# Question 2:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡¬Y-1.
# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]] 

def generates_2_dimensional_array(rows,cols):
  arr = [[i*j for i in range(cols)] for j in range(rows)]
  return arr

# Question 3:
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world

def sorting_alphabetically(test):
  x = sorted(test)
  return x

# Question 4:
# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

def sorting_alphanumerically(test):
  k=test.split(" ")
  l=list(set(k))
  l.sort()
  result=" ".join(l)
  return result

# Question 5:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123
# Then, the output should be:
# LETTERS 10
# DIGITS 3

def calculate_number_letters_digits(test):
  dc=0
  ac=0
  for i in test:
    if i.isalpha():
      ac+=1
    elif i.isdigit():
      dc+=1
  return "LETTERS",ac,"DIGITS ",dc

# Question 6:
# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
import re
test=["ABd1234@1","aF1#","2w3E*","2We3345"]
def passwords_checker(testing):
  res=[]
  for test in testing:
    k=re.findall("[A-Z]",test)
    l=re.findall("[a-z]",test)
    m=re.findall("[0-9]",test)
    n=re.findall("[@#$]",test)
    x=[len(k)>=1,len(l)>=1,len(m)>=1,len(n)>=1,len(test)>=6,len(test)<=12]
    if all(x):
      res.append(test)
  return ", ".join(res)
passwords_checker(test)

