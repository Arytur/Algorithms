# Python Program for recursive binary search.
# Returns index of x in arr if present, else -1

def binary_search (array, left, right, searching_number):
    # Check base case, continue while it is true, otherwise searching number
    # is not in the array
    if right >= left:
        middle = left + (right - left) // 2
        # If element is present at the middle itself
        if array[middle] == searching_number:
            return "Element is present at index %d" % middle
        # If element is smaller than mid, then it
        # can only be present in left subarray
        elif array[middle] > searching_number:
            return binary_search(array, left, middle - 1, searching_number)
        # Else the element can only be present
        # in right subarray
        else:
            return binary_search(array, middle + 1, right, searching_number)
    else:
        # Element is not present in the array
        return "Element is not present in array"

# Test arrays
arr = [2, 3, 4, 10, 40]
x = 10

arr2 = [2, 4, 5, 66, 67, 77, 89, 101, 155, 201, 300, 302, 304, 455, 701, 1002]
x2 = 455

# Function call
print(binary_search(arr, 0, len(arr) - 1, x))
print(binary_search(arr2, 0, len(arr2) - 1, x2))
