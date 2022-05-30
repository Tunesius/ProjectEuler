# n! means n × (n − 1) × ... × 3 × 2 × 1
#
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
#
# Find the sum of the digits in the number 100!

def add(n_string, second_n_string):
    transfer = ""
    complete_sum = ""
    reverse_n = n_string[::-1]
    second_reverse_n = second_n_string[::-1]
    largest = reverse_n
    smallest = second_reverse_n

    if len(second_reverse_n) > len(n_string):
        largest = second_reverse_n
        smallest = reverse_n

    for i in range(len(largest)):
        if i >= len(smallest):
            if transfer == "":
                temp_sum = str(int(largest[i]))
            else:
                temp_sum = str(int(largest[i]) + int(transfer))
        else:
            if transfer == "":
                temp_sum = str(int(reverse_n[i]) + int(second_reverse_n[i]))
            else:
                temp_sum = str(int(reverse_n[i]) + int(second_reverse_n[i]) + int(transfer))
        complete_sum = temp_sum[-1] + complete_sum
        transfer = temp_sum[:-1]
    complete_sum = transfer + complete_sum
    return complete_sum


current_product = "100"
for i in range(99, 0, -1):
    current_add = current_product
    for j in range(i):
        current_product = add(current_product, current_add)

print(current_product)

total_sum = 0
for c in current_product:
    total_sum = total_sum + int(c)

print(total_sum)
