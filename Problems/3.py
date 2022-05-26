# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

current_number_to_check = 600851475143
current_check_number = 2
list_of_prime_factors = []

while current_check_number <= current_number_to_check:
    if current_number_to_check % current_check_number == 0:
        list_of_prime_factors.append(current_check_number)
        current_number_to_check = current_number_to_check / current_check_number
        current_check_number = 1
    current_check_number = current_check_number + 1

print(list_of_prime_factors[len(list_of_prime_factors) - 1])
