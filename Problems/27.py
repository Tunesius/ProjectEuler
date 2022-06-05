# Euler discovered the remarkable quadratic formula:
#
#
# It turns out that the formula will produce 40 primes for the consecutive integer values . However, when  is divisible by 41, and certainly when  is clearly divisible by 41.
#
# The incredible formula  was discovered, which produces 80 primes for the consecutive values . The product of the coefficients, −79 and 1601, is −126479.
#
# Considering quadratics of the form:
#
# , where  and
#
# where  is the modulus/absolute value of
# e.g.  and
# Find the product of the coefficients,  and , for the quadratic expression that produces the maximum number of primes for consecutive values of , starting with .


def is_prime(n):
    result = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            result.add(j)
            result.add(n//j)
    result.discard(n)
    return not len(result) > 1


def find_primes_until_n(n=1000):
    list_of_primes = []
    for ii in range(2, n):
        if is_prime(ii):
            list_of_primes.append(ii)
    return list_of_primes


def find_amount_of_consecutive_primes(a, b):
    found_non_prime = False
    prime_counter = 0
    while not found_non_prime:
        current_value = prime_counter*prime_counter + a*prime_counter + b
        if current_value > 0 and is_prime(current_value):
            prime_counter = prime_counter + 1
        else:
            found_non_prime = True
    return prime_counter


list_of_b_values = find_primes_until_n()
print(list_of_b_values)

highest_prime_count = 0
correct_result = 0
for i in range(len(list_of_b_values)):
    for j in range(-999, 1000):
        current_prime_count = find_amount_of_consecutive_primes(j, list_of_b_values[i])
        if current_prime_count > highest_prime_count:
            highest_prime_count = current_prime_count
            correct_result = list_of_b_values[i]*j
print(correct_result)

