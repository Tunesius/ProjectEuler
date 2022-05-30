# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

def divisors(n):
    result = set()
    for j in range(1, int(n**0.5)+1):
        if n % j == 0:
            result.add(j)
            result.add(n//j)
    result.discard(n)
    return result


def give_divisor_sum(n):
    divisor_list = divisors(n)
    divisor_sum = 0
    for n in divisor_list:
        divisor_sum = divisor_sum + n
    return divisor_sum


total_number_sum = 0


for i in range(1, 10000):
    temp_sum = give_divisor_sum(i)
    if give_divisor_sum(temp_sum) == i and temp_sum != i:
        total_number_sum = total_number_sum + i

print(total_number_sum)
