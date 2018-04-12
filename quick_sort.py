import unittest

# Python program for sorting an array by using quick sort algorithm


def quick_sort(array):

    # If length of array is 0 or 1 then is nothing to sort, just return the array
    if len(array) < 2:
        return array
    else:
        # selecting first item from array, which is needed to compare the rest of numbers of array
        pivot = array[0]
        print("pivot", pivot)
        # here is an array of numbers less than pivot
        less = [i for i in array[1:] if i < pivot]
        print("\tless: ", less)
        # here is an array of numbers greater than pivot
        greater = [j for j in array[1:] if j > pivot]
        print("\tgreater: ", greater)
        # Continue sorting with 'less' and 'greater' arrays, until their length is less than 2
        return quick_sort(less) + [pivot] + quick_sort(greater)


print(quick_sort([3, 55, 12, 24, 1, 0, 18]))
print(quick_sort([1, 4, 7, 2, 99, 0, 11, 13]))


class TestQuickSort(unittest.TestCase):

    test_array1 = [5, 12, 2, 88, 10, 103]
    test_array2 = [51, 301, 16, 222, 1010, 44, 119, 1005, 2013, 1, 0, 13, 169]

    def test_quick_sort(self):
        self.assertEqual(quick_sort(self.test_array1), [2, 5, 10, 12, 88, 103])
        self.assertEqual(quick_sort(self.test_array2),
                         [0, 1, 13, 16, 44, 51, 119, 169, 222, 301, 1005, 1010, 2013])

        self.assertEqual(quick_sort([1]), [1])
        self.assertEqual(quick_sort([]), [])
