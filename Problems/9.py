# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
import math


def is_in_list(number, p_list):
    for n3 in p_list:
        if number == n3:
            return True
    return False


largest_possible_number = 500
perfect_squares = []
product = 0
for n in range(largest_possible_number):
    perfect_squares.append((n + 1) * (n + 1))

for n in perfect_squares:
    for n2 in perfect_squares:
        if is_in_list((n + n2), perfect_squares) and \
                math.sqrt(n) + math.sqrt(n2) + math.sqrt(n + n2) == 1000:
            product = math.sqrt(n) * math.sqrt(n2) * math.sqrt(n + n2)

print(int(product))
