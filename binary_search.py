import time
import unittest


def binary_search_algorithm(list_of_numbers, number_to_find):
    low = 0
    high = len(list_of_numbers) - 1
    steps = 0
    start_time = time.time()

    while low <= high:
        middle = (low + high) // 2
        number_guess = list_of_numbers[middle]
        if number_guess == number_to_find:
            steps += 1
            elapsed_time = time.time() - start_time
            print("List: %s ... %s \tSearching number: %d\n Position: %d \tSteps: %d \tTime: %s"
                  % (list_of_numbers[:4], list_of_numbers[-4:], number_to_find, middle, steps, elapsed_time))
            return middle
        if number_guess > number_to_find:
            high = middle - 1
            steps += 1
        else:
            low = middle + 1
            steps += 1
    return None


my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

binary_search_algorithm(my_list, 3)
binary_search_algorithm(my_list, 9)
binary_search_algorithm(my_list, -1)


class TestBinarySearch(unittest.TestCase):

    big_list_test = list(range(0, 251))
    big_list_three_step_test = list(range(0, 1001, 3))

    def test_binary_search_algorithm(self):
        self.assertEqual(binary_search_algorithm([], 5), None)

        self.assertEqual(binary_search_algorithm(self.big_list_test, 18), 18)
        self.assertEqual(binary_search_algorithm(self.big_list_test, 77), 77)

        self.assertNotEqual(binary_search_algorithm(self.big_list_test, 199), 100)
        self.assertNotEqual(binary_search_algorithm(self.big_list_test, 250), 251)

        self.assertEqual(binary_search_algorithm(self.big_list_test, -1), None)
        self.assertEqual(binary_search_algorithm(self.big_list_test, 300), None)

    def test_binary_search_algorithm_big_array(self):
        self.assertEqual(binary_search_algorithm([], 5), None)

        self.assertEqual(binary_search_algorithm(self.big_list_three_step_test, 516), 172)
        self.assertEqual(binary_search_algorithm(self.big_list_three_step_test, 792), 264)

        self.assertNotEqual(binary_search_algorithm(self.big_list_three_step_test, 9), 12)
        self.assertNotEqual(binary_search_algorithm(self.big_list_three_step_test, 222), 1)

        self.assertEqual(binary_search_algorithm(self.big_list_three_step_test, -100), None)
        self.assertEqual(binary_search_algorithm(self.big_list_three_step_test, 1), None)

