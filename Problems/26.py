# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
import math


def count_recurring_cycle(n, m):
    result = ""
    list_of_divisors = [10]
    current_divide = n*10
    current_result = math.floor(current_divide / m)
    result = result + str(current_result)
    rest = current_divide % m
    while rest*10 not in list_of_divisors and rest != 0:
        current_divide = rest * 10
        list_of_divisors.append(current_divide)
        current_result = math.floor(current_divide / m)
        result = result + str(current_result)
        rest = current_divide % m

    if rest == 0:
        return 0
    for i in range(len(list_of_divisors)):
        if list_of_divisors[i] == rest*10:
            return len(result) - i


highest_cycle = 6
correct_number = 7
for n in range(1, 1000):
    current_cycle = count_recurring_cycle(1, n)
    if current_cycle > highest_cycle:
        highest_cycle = current_cycle
        correct_number = n
print(correct_number)