def array_length_recursive(array):

    if not array:
        return 0
    else:
        return 1 + array_length_recursive(array[1:])


print(array_length_recursive([1, 4, 5, 6, 7, 12, 23, 54, 56, 445]))
print(array_length_recursive([]))
