# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

# First twenty digits: one, two, three, four (15), five, six, seven. eight (17), nine, ten, eleven, twelve (19), fourteen, fifteen (15), sixteen, seventeen (16), eighteen, nineteen, twenty (22)
# one thousand = 11

def give_special_count(n_string):
    if n_string[0] == "1":
        return 6
    elif n_string[0] == "2":
        return 6
    elif n_string[0] == "3":
        return 8
    elif n_string[0] == "4":
        return 8
    elif n_string[0] == "5":
        return 7
    elif n_string[0] == "6":
        return 7
    elif n_string[0] == "7":
        return 9
    elif n_string[0] == "8":
        return 8
    elif n_string[0] == "9":
        return 8
    return 3


def give_letter_count(n_string):
    if len(n_string) == 1:
        if n_string[0] == "1":
            return 3
        elif n_string[0] == "2":
            return 3
        elif n_string[0] == "3":
            return 5
        elif n_string[0] == "4":
            return 4
        elif n_string[0] == "5":
            return 4
        elif n_string[0] == "6":
            return 3
        elif n_string[0] == "7":
            return 5
        elif n_string[0] == "8":
            return 5
        elif n_string[0] == "9":
            return 4
        return 0

    if len(n_string) == 2:
        sum_of_letters = 0
        if n_string[0] == "0":
            sum_of_letters = sum_of_letters + give_letter_count(n_string[1])
        elif n_string[0] == "1":
            sum_of_letters = sum_of_letters + give_special_count(n_string[1])
        elif n_string[0] == "2":
            sum_of_letters = sum_of_letters + 6 + give_letter_count(n_string[1])
        elif n_string[0] == "3":
            sum_of_letters = sum_of_letters + 6 + give_letter_count(n_string[1])
        elif n_string[0] == "4":
            sum_of_letters = sum_of_letters + 5 + give_letter_count(n_string[1])
        elif n_string[0] == "5":
            sum_of_letters = sum_of_letters + 5 + give_letter_count(n_string[1])
        elif n_string[0] == "6":
            sum_of_letters = sum_of_letters + 5 + give_letter_count(n_string[1])
        elif n_string[0] == "7":
            sum_of_letters = sum_of_letters + 7 + give_letter_count(n_string[1])
        elif n_string[0] == "8":
            sum_of_letters = sum_of_letters + 6 + give_letter_count(n_string[1])
        elif n_string[0] == "9":
            sum_of_letters = sum_of_letters + 6 + give_letter_count(n_string[1])
        return sum_of_letters

    if n_string[1::] == "00":
        return 7 + give_letter_count(n_string[0]) + give_letter_count(n_string[1::])
    else:
        return 10 + give_letter_count(n_string[0]) + give_letter_count(n_string[1::])

total_sum = 0

temp_sum = 0
for i in range(100):
    print("now: " + str(i))

    total_sum = total_sum + give_letter_count(str(i))
    temp_sum = temp_sum + give_letter_count(str(i))

temp_sum_high = 0
for i in range(100, 1000):
    print("now: " + str(i))

    total_sum = total_sum + give_letter_count(str(i))
    temp_sum_high = temp_sum_high + give_letter_count(str(i))

total_sum = total_sum + 3 + 8

print("1-99: " + str(temp_sum))
print("100-999: " + str(temp_sum_high))
print("total sum: " + str(total_sum))




