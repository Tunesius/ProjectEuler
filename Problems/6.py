# The sum of the squares of the first ten natural numbers is,
#
# The square of the sum of the first ten natural numbers is,
#
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_numbers = 50 * 101
square_of_sum = sum_of_numbers * sum_of_numbers
sum_of_squares = 0

for n in range(100):
    sum_of_squares = sum_of_squares + ((n + 1) * (n + 1))


print(square_of_sum - sum_of_squares)
