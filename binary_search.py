import time

def binary_search(list_of_numbers, number_to_find):
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
            result = """List: %s ... %s \tSearching number: %d\n
                    Position: %d \tSteps: %d \tTime: %s
                         """ % (list_of_numbers[:4], list_of_numbers[-4:],
                         number_to_find, middle, steps, elapsed_time)
            return result
        if number_guess > number_to_find:
            high = middle - 1
            steps += 1
        else:
            low = middle + 1
            steps += 1
    return None

my_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35]

print(binary_search(my_list, 3))
print(binary_search(my_list, 9))
print(binary_search(my_list, -1))

big_list = list(range(0, 251))

print(binary_search(big_list, 18))
print(binary_search(big_list, 77))
print(binary_search(big_list, 199))
print(binary_search(big_list, 250))

big_list_three_step = list(range(0, 1001, 3))
print(binary_search(big_list_three_step, 516))
print(binary_search(big_list_three_step, 792))
print(binary_search(big_list_three_step, 9))
print(binary_search(big_list_three_step, 222))
