def array_max_number_recursive(array):

    if len(array) == 1:
        return array[0]
    else:
        if array[0] < array[1]:
            array.pop(0)
            return array_max_number_recursive(array)
        else:
            array.pop(1)
            return array_max_number_recursive(array)


print(array_max_number_recursive([1, 4, 5, 6, 7, 12, 1002, 23, 540, 56, 445]))
print(array_max_number_recursive([100, 41, 5, 66, 7, 12, 102, 23, 540, 56, 445]))