# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?
prime_number_list = [2, 3]
current_prime_number_count = 2
current_number = 5

def is_dividable_by_prime(number):
    for n in prime_number_list:
        if number % n == 0:
            return True
    return False

while current_prime_number_count < 10001:

    if not is_dividable_by_prime(current_number):
        current_prime_number_count = current_prime_number_count + 1
        prime_number_list.append(current_number)
    current_number = current_number + 1

print(prime_number_list[10000])
