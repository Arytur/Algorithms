def find_smallest(array):
    smallest = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    new_array = []
    for i in range(len(array)):
        smallest = find_smallest(array)
        new_array.append(array.pop(smallest))
    return new_array

print('\n[5, 3, 6, 2, 10]')
print(selection_sort([5, 3, 6, 2, 10]))
print('\n[51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]')
print(selection_sort([51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]))
