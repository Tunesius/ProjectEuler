#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
#Find the largest palindrome made from the product of two 3-digit numbers.
import math

current_number_one = 100
current_number_two = 100
current_largest_palindrome = 0


def is_palindrome(number):
    number_string = str(number)
    length_of_number = len(number_string)
    length_to_look_at = math.floor(length_of_number / 2)
    for n in range(length_to_look_at):
        if number_string[n] != number_string[-n - 1]:
            return False
    return True


while current_number_one < 1000:
    current_number_two = current_number_one + 1
    while current_number_two < 1000:
        current_product = current_number_two * current_number_one
        if is_palindrome(current_product):
            if current_product > current_largest_palindrome:
                current_largest_palindrome = current_product
        current_number_two = current_number_two + 1
    current_number_one = current_number_one + 1


print(current_largest_palindrome)



