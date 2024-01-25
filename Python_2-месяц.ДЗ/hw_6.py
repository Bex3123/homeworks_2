def selection_sort(lst):
    for i in range(len(lst)):
        mn = min(range(i, len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], lst[i]

    return lst

def binary_search(sorted_lst, val):
    first = 0
    last = len(sorted_lst) - 1
    position = None

    while first <= last:
        middle = (first + last) // 2
        if val == sorted_lst[middle]:
            position = middle
            break
        elif val > sorted_lst[middle]:
            first = middle + 1
        else:
            last = middle - 1

    if position is not None:
        return f'{val} exists at position {position}'
    else:
        return f'{val} does not exist'

my_list = [18, 54, 274, 31, 44, 23, 87, 96, 52, 74, 258, 412, 961, 24, 96]
sorted_list = selection_sort(my_list)
print(sorted_list)
print(binary_search(sorted_list, 87))
print(binary_search(sorted_list, 0))
print(binary_search(sorted_list, 31))
