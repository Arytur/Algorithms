import unittest

# Python Program for recursive binary search.
# Returns index of x in arr if present, else -1


def recursive_binary_search(array, left, right, searching_number):

    print(array[left:right + 1])

    # Check base case, continue while it is true, otherwise searching number
    # is not in the array
    if right >= left:
        middle = left + (right - left) // 2

        # If element is present at the middle itself
        if array[middle] == searching_number:
            print("Element is present at index %d" % middle)
            return middle
        # If element is smaller than mid, then it
        # can only be present in left subarray

        elif array[middle] > searching_number:
            return recursive_binary_search(array, left, middle - 1, searching_number)
        # Else the element can only be present
        # in right subarray

        else:
            return recursive_binary_search(array, middle + 1, right, searching_number)

    else:
        # Element is not present in the array
        print("Element is not present in array")
        return None


# Test arrays
arr = [2, 3, 4, 10, 40, 50, 60, 85, 100]

# Function call
print(recursive_binary_search(arr, 0, len(arr) - 1, 10))


class TestRecursiveBinarySearch(unittest.TestCase):

    test_array = [2, 4, 5, 66, 67, 77, 89, 101, 155, 201]
    test_big_array = list(range(0, 1000, 2))

    def test_recursive_binary_search_small_array(self):
        self.assertEqual(recursive_binary_search([], 1, 0, 5), None)

        self.assertEqual(recursive_binary_search(self.test_array, 0, len(self.test_array) - 1, 67), 4)
        self.assertEqual(recursive_binary_search(self.test_array, 0, len(self.test_array) - 1, 2), 0)

        self.assertNotEqual(recursive_binary_search(self.test_array, 0, len(self.test_array) - 1, 4), 5)
        self.assertNotEqual(recursive_binary_search(self.test_array, 0, len(self.test_array) - 1, 101), 8)

        self.assertEqual(recursive_binary_search(self.test_array, 0, len(self.test_array) - 1, -55), None)
        self.assertEqual(recursive_binary_search(self.test_array, 0, len(self.test_array) - 1, 55), None)

    def test_recursive_binary_search_big_array(self):
        self.assertEqual(recursive_binary_search([], 1, 0, 5), None)

        self.assertEqual(recursive_binary_search(self.test_big_array, 0, len(self.test_big_array) - 1, 998), 499)
        self.assertEqual(recursive_binary_search(self.test_big_array, 0, len(self.test_big_array) - 1, 2), 1)

        self.assertNotEqual(recursive_binary_search(self.test_big_array, 0, len(self.test_big_array) - 1, 4), 5)
        self.assertNotEqual(recursive_binary_search(self.test_big_array, 0, len(self.test_big_array) - 1, 101), 8)

        self.assertEqual(recursive_binary_search(self.test_big_array, 0, len(self.test_big_array) - 1, -55), None)
        self.assertEqual(recursive_binary_search(self.test_big_array, 0, len(self.test_big_array) - 1, 55), None)
