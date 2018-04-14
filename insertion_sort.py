# Python program for sorting an array by using insertion sort algorithm

import unittest


def insertion_sort(array):
    # At the begging we assume that element with index 0 is already sorted
    for index in range(1, len(array)):
        # Creating a variable to keep the value for current element to sort
        current_value = array[index]
        position = index

        # Shifting elements of sorted sublist until they are greater than current value
        while position > 0 and array[position - 1] > current_value:
            array[position] = array[position - 1]
            position -= 1

        # After while loop is done, insert the value in the right position
        array[position] = current_value
    return array


print(insertion_sort([3, 55, 12, 24, 1, 0, 18]))
print(insertion_sort([1, 4, 7, 2, 99, 0, 11, 13]))


class TestInsertionSort(unittest.TestCase):

    test_array1 = [5, 12, 2, 88, 10, 103]
    test_array2 = [51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]

    def test_quick_sort(self):
        self.assertEqual(insertion_sort(self.test_array1), [2, 5, 10, 12, 88, 103])
        self.assertEqual(insertion_sort(self.test_array2),
                         [0, 1, 13, 16, 44, 51, 119, 169, 222, 301, 1005, 1010, 2013])

        self.assertEqual(insertion_sort([1]), [1])
        self.assertEqual(insertion_sort([]), [])