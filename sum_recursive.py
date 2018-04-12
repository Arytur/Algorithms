def array_sum_recursive(array):

    if len(array) > 1:
        return array.pop(0) + array_sum_recursive(array)
    else:
        return array[0]


print(array_sum_recursive([2, 14, 44, 101, 555]))
print(array_sum_recursive([202, 104, 44, 1201, 56]))
