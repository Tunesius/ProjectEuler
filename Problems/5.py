# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
import math

current_number = 20
max_number = math.factorial(20)
correct_number = max_number

while current_number <= max_number:
    if (current_number % 11 == 0 and
            current_number % 12 == 0 and
            current_number % 13 == 0 and
            current_number % 14 == 0 and
            current_number % 15 == 0 and
            current_number % 16 == 0 and
            current_number % 17 == 0 and
            current_number % 18 == 0 and
            current_number % 19 == 0 and
            current_number % 20 == 0):
        correct_number = current_number
        current_number = max_number + 1
    else:
        current_number = current_number + 1


print(correct_number)