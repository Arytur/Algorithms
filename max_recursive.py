def array_max_number_recursive(array):

    if len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    sub_max = array_max_number_recursive(array[1:])
    return array[0] if array[0] > sub_max else sub_max


print(array_max_number_recursive([1, 4, 5, 6, 7, 12, 1002, 23, 540, 56, 445]))
print(array_max_number_recursive([100, 41, 5, 66, 7, 12, 102, 23, 540, 56, 445]))