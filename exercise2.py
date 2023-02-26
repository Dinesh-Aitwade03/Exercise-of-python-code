# # 51. Write a Python program to determine the profiling of Python programs.
# Note: A profile is a set of statistics that describes how often and for how long various parts of the
# program executed.
# These statistics can be formatted into reports via the pstats module.

# import cProfile
# def sum():
#     print(1+2)
# cProfile.run('sum()')

# 58. Write a Python program to sum the first n positive integers
# n = int(input('enter num:'))
# print((n*(n+1))/2)

# 68. Write a Python program to calculate sum of digits of a number
# num = int(input("enter number="))
# num = str(num)
# sum = 0
# for i in num:
#     sum =sum+int(i)
# print(sum)
# ---------------------------
# num = int(input("Input a four digit numbers: "))
# x  = num //1000
# x1 = (num - x*1000)//100
# x2 = (num - x*1000 - x1*100)//10
# x3 = num - x*1000 - x1*100 - x2*10
# print("The sum of digits in the number is", x+x1+x2+x3)


# 69. Write a Python program to sort three integers without using conditional statements and loops.
# num1 = int(input("enter num1="))
# num2 = int(input("enter num2="))
# num3 = int(input("enter num3="))
#
# maxx = max(num1,num2,num3)
# minn = min(num1,num2,num3)
# midd = (num1+num2+num3)-maxx-minn
# print(maxx,midd,minn)

# Write a Python program to concatenate N strings.
# lst = ['a','b','c']
# print('-

# 82. Write a Python program to calculate the sum of all items of a container
# (tuple, list, set, dictionary).
# dict = {'a':10,'b':20}
# summ = 0
# for i in dict.values():
#     summ = summ+i
# print(summ)


# 83. Write a Python program to test whether all numbers in a list are greater than a certain number.

# lstt = [1,2,3,4,5,6,7,8]
# lst_min = min(lstt)
# print(lst_min)
# num = int(input('enter num='))
# if lst_min > num:
#     print('True')
# else:
#     print('False')

# 84. Write a Python program to count the number of occurrences of a specific character in a string.
# strr = 'dinesh aitwadeadfdkfmeijawemcc'
# cnt = strr.count('a')
# print(cnt)

# 86. Write a Python program to get the ASCII value of a character.
# a='a'
# print(ord(a))

#
# 87. Write a Python program to get the size of a file.
# import os
# file_size = os.path.getsize("abc.txt")
# print("\nThe size of abc.txt is :",file_size,"Bytes")
# print()

# 88. Given variables x=30 and y=20, write a Python program to print "30+20=50".
# x=30
# y=20
# summ = x+y
# print(f'"{x}+{y}={summ}"')

# 90. Write a Python program to create a copy of its own source code
# def file_copy(src, dest):
#     with open(src) as f, open(dest, 'w') as d:
#         d.write(f.read())
#         file_copy("untitled0.py", "z.py")
#         with open('z.py', 'r') as filehandle:
#             for line in filehandle:
#                 print(line, end = '')

# 91. Write a Python program to swap two variables.
# a=1
# b=2
# a,b=b,a
# print(a,b)

# 92. Write a Python program to define a string containing special characters in various forms.
# str = 'fdskj234994&@#$*(UJnfcefhw839*$&^@$&)*('
# for i in str:
#     if i.isalnum():
#         pass
#     else:
#         print('have special char',i)

# 9)3. Write a Python program to get the Identity, Type, and Value of an object.
# a=10
# print(id(a),type(a),a)

# 94. Write a Python program to convert the bytes in a given string to a list of integers.
# a=b'abc'
# lss=list(a)
# print(lss)

# 95. Write a Python program to check whether a string is numeric.
# str = 'a234ghh'
# if str.isdigit():
#     print('numeric')
# else:
#     print('no numeric')

# 110. Write a Python program to get numbers divisible by fifteen from a list using an anonymous function.

# lst = [434,5555,563675,435,677,65440,150]
# div_num = list(filter(lambda x : x%15==0,lst))
# print(div_num)

# 112. Write a Python program to remove the first item from a specified list
# lstt = [1,2,3]
# lstt.pop(0)
# print(lstt)

#  113. Write a Python program that inputs a number and generates
#  an error message if it is not a number
# while True:
#     try:
#
#        num = int(input('enter num='))
#        break
#     except ValueError:
#         print('this is not a number')

# 114. Write a Python program to filter positive numbers from a list.
# numlst=[1,2,-3,-4,-5]
# pos_num = list(filter(lambda x:x>0,numlst))
# print(pos_num)

# 115. Write a Python program to compute the product of a list of integers (without using a for loop
# from functools import reduce
#
# lstt = [1,2,3,4,5]
# pro = reduce(lambda x,y:x*y,lstt)
# print(pro)


# 116. Write a Python program to print Unicode characters
# str = u'\u0050\u0079\u0074\u0068\u006f\u006e \u0045\u0078\u0065\u0072\u0063\u0069\u0073\u0065\u0073 \u002d \u0077\u0033\u0072\u0065\u0073\u006f\u0075\u0072\u0063\u0065'
# print()
# print(str)

# 117. Write a Python program to prove that two string variables of
# the same value point to the same memory location
# a='dinesh'
# b='dinesh'
# print(id(a),id(b),end='\t')

# 118. Write a Python program to create a bytearray from a list.
# lss = [1,2,3]
# print(bytearray(lss))

# 119. Write a Python program to round a floating-point number to a
# specified number of decimal places.
# def round(x):
#     print('%.2f'% x)
# round(10.5)

# 120. Write a Python program to format a specified string and limit
# the length of a string.

# str = '123456789'
# print('%.6s'%str)
# print('%.2s'%str)
# print('%.4s'%str)

# 121. Write a Python program to determine if a variable is defined or not.
# try:
#     xml
#
# except NameError:
#     print('variable is not defined')

# 122. Write a Python program to empty a variable without destroying it.

# n = 20
# d = {"x":200}
# l = [1,3,5]
# t= (5,7,8)
# print(type(n)())
# print(type(d)())
# print(type(l)())
# print(type(t)())

# Expected Output : 0
# {}

# 124. Write a Python program to check whether multiple variables have the same value
# a =int(input('num1='))
# b = int(input('num2='))
# c=int(input('num3='))
# if a==b==c:
#     print('same value')
# else:
#     print('not same')


# 125. Write a Python program to sum all counts in a collection
# from collections import Counter
#
# lll = [1,2,3,4,4,12,3,4,4,5,6,7,8,56,54,3,4,5,6,7]
# cnt = Counter(lll)
# print(cnt)
# print(sum(cnt.values()))
# print(len(lll))

# 128. Write a Python program to check whether lowercase letters exist in a string.
# ss = 'ESH'
# for i in ss:
#
#     if i.islower():
#         print('lower')
#         break
# else:
#
#     print('nolower')

# 129. Write a Python program to add leading zeroes to a string
# srr = '12345'
# # print(srr.ljust(2,'#'))  # o/p--12345
# # print(srr.ljust(8,'#'))  # o/p--12345###
# # print(srr.rjust(2,'#'))
# # print(srr.rjust(8,'#'))

# 130. Write a Python program that uses double quotes to display strings
# import json
# print(json.dumps({'Alex': 1, 'Suresh': 2, 'Agnessa': 3}))

# 133. Write a Python program to calculate the time runs
# (difference between start and current time) of a program.

# from timeit import default_timer
# def timer(n):
#     start = default_timer()
#     # some code here
#     for row in range(0,n):
#         print(row)
#     print(default_timer() - start)
#
# timer(5)
# timer(15)

# 134. Write a Python program to input two integers on a single line.
# x, y = map(int, input().split(' '))
# print(x,y)

# 137. Write a Python program to extract a single key-value pair from a dictionary into variables
# dicc = {1:'dinesh',2:'ram',3:'sham'}
# for a,b in dicc.items():
#     print(a,b,sep=':')

# 138. Write a Python program to convert true to 1 and false to 0.
# print(int(True))
# print(int(False))

# 142. Write a Python program to check if every consecutive sequence of zeroes is followed
# by a consecutive sequence of ones of same length in a given string. Return True/False. Go to the editor
# Original sequence: 01010101
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones
# the said string:
# True
# Original sequence: 00
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in
# the said string:
# False
# Original sequence: 000111000111
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in
# the said string:
# True
# Original sequence: 00011100011
# Check if every consecutive sequence of zeroes is followed by a consecutive sequence of ones in the said string:
# False

# seq = '01'
# while '01' in seq:
#
#     seq = seq.replace('01','')
# print(seq)
# if len(seq)==0:
#     print('True')
# else:
#     print('false')

# 144. Write a Python program to check whether a variable is an integer or string.
# a='10'
# if type(a)==int:
#     print('integer')
# elif type(a)==str:
#     print('string')

# 147. Write a Python function to check whether a number is
# divisible by another number. Accept two integer values from the user
# num1=int(input('='))
# num2 = int(input("="))
# if num1%num2==0 or num2%num1==0:
#     print('no is divisible by another num')
# else:
#     print('not divisible')

# 148. Write a Python function to find the maximum and minimum numbers from a sequence of numbers
# Note: Do not use built-in functions.
# def max_min(data):
#     l=data[0]
#     s = data[0]
#     for i in data:
#         if i>l:
#             l =i
#         elif i<s:
#             s = i
#     return l,s
# print(max_min([1,2,3,4,6,-4]))

# 149. Write a Python function that takes a positive integer and returns
# the sum of the cube of all positive integers smaller than the that integer.
# def cubes(n):
#     resul = 0
#     while n>0:
#         resul = resul+(n**3)
#         n-=1
#     print(resul)
# cubes(2)

