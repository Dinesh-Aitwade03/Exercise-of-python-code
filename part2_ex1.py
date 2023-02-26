# 1. Write a Python function that takes a sequence of numbers and determines
# whether all the numbers are different from each other.

# def num_diff(seq):
#     seq = list(seq)
#     check_seq = []
#     for i in seq:
#         if i not in check_seq:
#             check_seq.append(i)
#
#
#         else:
#             print('There is repetation in numbers')
#             break
#
#
# a= [1,2,3,4,6]
# num_diff(a)
# b=[1,2,3,2]
# num_diff(b)

# -------------------------
# def distinct(data):
#   if len(data) == len(set(data)):
#     return True
#   else:
#     return False;
# print(distinct([1,5,7,9]))
# print(distinct([2,4,5,5,7,9]))

#2. Write a Python program that creates all possible strings using the letters 'a', 'e', 'i', 'o', and 'I'.
# Ensure that each character is used only once

# import random
# char_list = ['a','e','i','o','u']
# for i in range(1,len(char_list)+1):
#
#     random.shuffle(char_list)
#     print(''.join(char_list))

#3. Write a Python program that removes and prints every third number from a list of numbers until
# the list is empty.
# try:
#     llt = [1,2,3,4,5,6]
#     for i in range(0,len(llt)):
#         print(llt[2])
#         llt.pop(2)
# except IndexError:
#     llt = []
#------------------------------------
# def remove_nums(int_list):
#   #list starts with 0 index
#   position = 3 - 1
#   idx = 0
#   len_list = (len(int_list))
#   while len_list>0:
#     idx = (position+idx)%len_list
#     print(int_list.pop(idx))
#     len_list -= 1
# nums = [10,20,30,40,50,60,70,80,90]
# remove_nums(nums)

# 4. Write a Python program to identify unique triplets whose three elements sum to zero
# from an array of n integers
# def three_sum(nums):
#   result = []
#   nums.sort()
#   for i in range(len(nums)-2):
#     if i> 0 and nums[i] == nums[i-1]:
#       continue
#     l, r = i+1, len(nums)-1
#     while l < r:
#       s = nums[i] + nums[l] + nums[r]
#       if s > 0:
#         r -= 1
#       elif s < 0:
#           l += 1
#       else:
#         # found three sum
#         result.append((nums[i], nums[l], nums[r]))
#         # remove duplicates
#         while l < r and nums[l] == nums[l+1]:
#           l+=1
#           while l < r and nums[r] == nums[r-1]:
#             r -= 1
#             l += 1
#             r -= 1
#           return result
#
# x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
# print(three_sum(x))


# 5. Write a Python program to make combinations of 3 digits.
# for i in range(100,1000):
#     i=str(i)
#     if i[0]==i[1]==i[2]:
#         print(i)
# ------------------------------
# numbers = []
# for num in range(1000):
#   num=str(num).zfill(3)
# print(num)
# numbers.append(num)

# 6. Write a Python program that prints long text, converts it to a list,
# and prints all the words and the frequency of each word
from collections import Counter
a= '''Save your favorite articles to read offline, sync your 
   reading lists across devices and customize your reading experience with the official Wikipedia app.'''

# print(a)
# lst1 = a.split(" ")
# print(lst1)
# dct = Counter(lst1)
# print(dct)


# 7. Write a Python program to count the number of each character in a text file.

# import collections
# import pprint
# file_input = input('File Name: ')
# with open(file_input, 'r') as info:
#   count = collections.Counter(info.read().upper())
#   value = pprint.pformat(count)
# print(value)

# 12. Write a Python program that generates a list of all possible permutations from
# a given collection of distinct numbers.

# def permute(nums):
#   result_perms = [[]]
#   for n in nums:
#     new_perms = []
#     for perm in result_perms:
#       for i in range(len(perm)+1):
#         new_perms.append(perm[:i] + [n] + perm[i:])
#         result_perms = new_perms
#   return result_perms
#
# my_nums = [1,2,3]
# print("Original Cofllection: ",my_nums)
# print("Collection of distinct numbers:\n",permute(my_nums))

# 14. Write a Python program to add two positive integers without using the '+' operator.
# def add_without_plus_operator(a, b):
#     while b != 0:
#         data = a & b
#         a = a ^ b
#         b = data << 1
#     return a
# print(add_without_plus_operator(2, 10))
# print(add_without_plus_operator(-20, 10))
# print(add_without_plus_operator(-10, -20))

# 18. Write a Python program to find the median among three given numbers.

# x = int(input('enter 1st num='))
# y = int(input('enter 1st num='))
# z = int(input('enter 1st num='))
# if x>y and y>z:
#     print(y)
# elif x>z and z>y:
#     print(z)
# elif z>x and x>y:
#     print(x)
# elif z>y and y>x:
#     print(y)
# elif y>x and x>z:
#     print(x)
# elif y>z and z>x:
#     print(z)

# 24. Write a Python program to find the total number of even or odd divisors of a given integer
# def divisor(n):
#   x = [i for i in range(1,n+1) if not n % i]
#   return x
# print(divisor(15))
# print(divisor(12))
# print(divisor(9))
# print(divisor(6))
# print(divisor(3))

# 25. Write a Python program to find the digits that are missing from a given mobile number.
# mob = '9403395251'
# miss_mob = "94033 5251"
# for i in range(0,len(mob)):
#     if mob[i]!=miss_mob[i]:
#         print(mob[i])

# -------------------------------------------
# lst = [0,1,2,3,4,5,6,7,8,9]
# mob_no = "940395251"
# for i in lst:
#     if str(i) not in mob_no:
#         print(i)

# 29. Write a Python program to find common divisors between two numbers in a given pair.
# def divisors(a,b):
#     minn = min(a,b)
#     co = []
#     for i in range(1,minn+1):
#         if a%i==0 and b%i==0:
#             co.append(i)
#     print(len(co))
#
# divisors(2,3)
# print()
# divisors(5,25)
# print()
# divisors(100,30)
# print()
# divisors(12,24)

# 30. Write a Python program to reverse the digits of a given number and add them to the original.
# Repeat this procedure if the sum is not a palindrome

# num = input('enter num=')
# newnum = num[::-1]
# print(newnum)
# sum=int(num)+int(newnum)
# print(sum)
# a= str(sum)
# b = a[::-1]
# print(a, b)
# if a == b:
#     print("palindrom")
# else:
#     print('not palindrom')

# 31.Write a Python program to count the number of carry operations for each addition problem.