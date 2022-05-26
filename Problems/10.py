# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.
prime_number_list = [2, 3]
sum_of_primes = 5
current_number = 5


def is_dividable_by_prime(number):
    for n in prime_number_list:
        if number % n == 0:
            return True
    return False


while current_number < 2000000:

    if not is_dividable_by_prime(current_number):
        prime_number_list.append(current_number)
        sum_of_primes = sum_of_primes + current_number
        print(current_number)

    current_number = current_number + 2



print(sum_of_primes)
