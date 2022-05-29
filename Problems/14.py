# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

def collatz(n):
    if n % 2 == 0:
        return n / 2
    return 3*n + 1


def give_collatz_count(n):
    c = 1
    while n != 1:
        n = collatz(n)
        c = c+1
    return c


def give_largest_collatz_number(n):
    max_count = 0
    max_number = 0
    for i in range(1, n+1):
        print(i)
        count = give_collatz_count(i)
        if count > max_count:
            max_count = count
            max_number = i
    return max_number


print(give_largest_collatz_number(1_000_000))
