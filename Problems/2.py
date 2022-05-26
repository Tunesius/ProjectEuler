# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

last_fibonacci_number = 1
current_fibonacci_number = 1
temp_number = 0
final_sum = 0

while current_fibonacci_number <= 4000000:
    temp_number = current_fibonacci_number
    current_fibonacci_number = current_fibonacci_number + last_fibonacci_number
    last_fibonacci_number = temp_number
    if current_fibonacci_number % 2 == 0:
        final_sum = final_sum + current_fibonacci_number

print(final_sum)