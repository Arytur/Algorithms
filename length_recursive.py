def array_length_recursive(array):
    length = 1

    if not array:
        return 0
    else:
        return length + array_length_recursive(array[length:])


print(array_length_recursive([1, 4, 5, 6, 7, 12, 23, 54, 56, 445]))
print(array_length_recursive([]))
