def double(n_string):
    transfer = "0"
    complete_sum = ""
    reverse_n = n_string[::-1]
    for c in reverse_n:
        if transfer == "":
            temp_sum = str(int(c) + int(c))
        else:
            temp_sum = str(int(c) + int(c) + int(transfer))
        complete_sum = temp_sum[-1] + complete_sum
        transfer = temp_sum[:-1]
    complete_sum = transfer + complete_sum
    return complete_sum


def give_power_of_two(n):
    result = "1"
    for i in range(n):
        result = double(result)
    return result


def add_digits(n_string):
    digit_sum = 0
    for c in n_string:
        digit_sum = digit_sum + int(c)
    return digit_sum


print(add_digits(give_power_of_two(1000)))
