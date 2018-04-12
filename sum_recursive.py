def array_sum_recursive(array):

    if not array:
        return 0
    else:
        return array[0] + array_sum_recursive(array[1:])


print(array_sum_recursive([2, 14, 44, 101, 555]))
print(array_sum_recursive([202, 104, 44, 1201, 56]))
