import unittest
import random

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
        print(new_array)
    # Return new sorted array
    return new_array


print('\n[5, 3, 6, 2, 10]')
print(selection_sort([5, 3, 6, 2, 10]))
random_array = [random.randint(0, 2550) for x in range(30)]
print('\n', random_array)
print(selection_sort(random_array))


class TestSelectionSort(unittest.TestCase):

    test_array1 = [5, 12, 2, 88, 10, 103]
    test_array2 = [51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]

    def test_find_smallest(self):
        self.assertEqual(find_smallest(self.test_array1), 2)
        self.assertEqual(find_smallest(self.test_array1[:1]), 0)

        self.assertEqual(find_smallest(self.test_array2), 10)
        self.assertEqual(find_smallest(self.test_array2[:5]), 2)

    def test_selection_sort(self):
        self.assertEqual(selection_sort(self.test_array1), [2, 5, 10, 12, 88, 103])
        self.assertEqual(selection_sort(self.test_array2),
                         [0, 1, 13, 16, 44, 51, 119, 169, 222, 301, 1005, 1010, 2013])

