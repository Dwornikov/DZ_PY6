def find_indices_in_range(lst, minimum, maximum):
    indices = list(filter(lambda i: minimum <= lst[i] <= maximum, range(len(lst))))
    return indices

my_list = [2, 5, 8, 11, 14]
min_value = 6
max_value = 12
result = find_indices_in_range(my_list, min_value, max_value)
print(result)
