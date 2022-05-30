def import_list_from_file(file_path):
    file = open(file_path)
    file_content = file.readline()
    file_content = file_content.replace('"', '')
    names = file_content.split(",")
    return names


def sort_list(plist):
    sorted_name_list = [plist[0]]
    plist.pop(0)
    for name in plist:
        current_index = 0
        while current_index < len(sorted_name_list) and name > sorted_name_list[current_index]:
            current_index = current_index + 1
        sorted_name_list.insert(current_index, name)
    return sorted_name_list


def give_letter_sum(pwort):
    letter_sum = 0
    for c in pwort:
        letter_sum = letter_sum + ord(c) - 64
    return letter_sum


sorted_list = sort_list(import_list_from_file("p022_names.txt"))
total_sum = 0
for i in range(len(sorted_list)):
    total_sum = total_sum + (give_letter_sum(sorted_list[i]) * (i + 1))
print(total_sum)




