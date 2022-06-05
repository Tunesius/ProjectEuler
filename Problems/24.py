# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
import math


def give_nth_permutation(n_string, n, p_permutation):
    if len(n_string) == 2:
        if n == 1:
            return p_permutation + n_string
        else:
            return p_permutation + n_string[::-1]
    else:
        permutation = p_permutation
        max_permutations = math.factorial(len(n_string))
        index_calculate = max_permutations / len(n_string)
        needed_index = math.floor((n-1)//index_calculate)
        new_n = math.floor(n - (needed_index * index_calculate))
        new_n_string = n_string.replace(n_string[needed_index], "")
        permutation = permutation + n_string[needed_index]
        print("n: " + str(n))
        print("max_permutations: " + str(max_permutations))
        print("index_calculate: " + str(index_calculate))
        print("needed_index: " + str(needed_index))
        print("new_n: " + str(new_n))
        print("new_n_string: " + str(new_n_string))
        print("permutation: " + str(permutation))

        print("NEXXT!!!")
        if new_n == 1:
            permutation = permutation + new_n_string
        else:
            permutation = give_nth_permutation(new_n_string, new_n, permutation)
        return permutation


print(give_nth_permutation("0123456789", 1_000_000, ""))

