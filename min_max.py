# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 10/08/2022
# Description: Write a program that asks the user how many integers they would like to enter.
# The program will then prompt the user to enter that many integers. After all the numbers have
# been entered, the program should display the largest and smallest of those numbers.

value = 0
index = 0
min = 0
max = 0

numb = int(input("How many integers would you like to enter?"))
print('Please enter', numb, 'integers.')
min = value
max = value
value = int(input())
while index < numb - 1:
    value = int(input(""))
    if value < min:
        min = value
    if value > max:
        max = value
    index = index + 1
print('min:', min, )
print('max:', max, )
