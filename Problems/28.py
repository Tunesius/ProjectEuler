current_value = 1
current_sum = 1
current_length = 1
current_side = 4
while not (current_length == 1001 and current_side == 4):
    if current_side == 4:
        current_length = current_length + 2
        current_side = 0
    current_value = current_value + (current_length-1)
    current_sum = current_sum + current_value
    current_side = current_side + 1
print(current_sum)

