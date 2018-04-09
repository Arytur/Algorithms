# Python program for sorting an array by selection

# Find the smallest element in the given array
def find_smallest(array):

    # Take element with index 0, and assign it to variable
    smallest = array[0]
    smallest_index = 0

    # Start 'for loop' from index 1
    for i in range(1, len(array)):

        # Compare element with index 'i' and current 'smallest' variable .
        # According to the comparision, assign new value to the 'smallest'
        # variable or continue with the current one.
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    # Return index of the smallest number to the 'selection_sort' function
    return smallest_index

# Create a new array for the sorted numbers
def selection_sort(array):
    new_array = []

    # Repeat for every element in the array
    for i in range(len(array)):

        # Call the 'find_smallest' function
        smallest = find_smallest(array)
        # Append returned value to the 'new_array' and remove it from original list
        new_array.append(array.pop(smallest))
    # Return new sorted array
    return new_array


print('\n[5, 3, 6, 2, 10]')
print(selection_sort([5, 3, 6, 2, 10]))
print('\n[51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]')
print(selection_sort([51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]))
