# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

def partition(l, r, nums):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swappping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr

# With quicksort() function, we will be utilizing the above code to obtain the pointer
# at which the left values are all smaller than the number at pointer index and vice versa
# for the right values.


def quicksort(l, r, nums):
    if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
        return nums
    if l < r:
        pi = partition(l, r, nums)
        quicksort(l, pi-1, nums)  # Recursively sorting the left values
        quicksort(pi+1, r, nums)  # Recursively sorting the right values
    return nums

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


def give_abundant_numbers(upper_limit):
    abundant_numbers = []
    for i in range(upper_limit):
        if give_divisor_sum(i) > i:
            abundant_numbers.append(i)
    return abundant_numbers


def is_sum(n, abundant_numbers):
    for ii in range(len(abundant_numbers) - 1):
        if abundant_numbers[ii] > n:
            break
        for j in range(ii, len(abundant_numbers)):
            if abundant_numbers[j] > n:
                break
            if abundant_numbers[ii] + abundant_numbers[j] == n:
                return True
    return False


def make_set_to_list(pset):
    returnlist = []
    for value in pset:
        returnlist.append(value)
    return returnlist


def give_all_sums(abundant_numbers):
    all_sum_set = set({})
    for number in range(len(abundant_numbers)):
        for number_two in range(number, len(abundant_numbers)):
            temp_sum = abundant_numbers[number] + abundant_numbers[number_two]
            if not temp_sum > 28123:
                all_sum_set.add(temp_sum)
    return all_sum_set


def is_in_list(n, plist):
    for number in plist:
        if number > n:
            return False
        elif number == n:
            return True
    return False


abundant_number_list = give_abundant_numbers(28123-12)
all_sums = make_set_to_list(give_all_sums(abundant_number_list))
all_sums.sort()

print(all_sums)
print(len(all_sums))

total_sum = 0
for i in range(28124):
    if not is_in_list(i, all_sums):
        print(i)
        total_sum = total_sum + i

print(total_sum)