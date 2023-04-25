'''
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
'''
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f'{hours:02d}:{minutes:02d}:{seconds:02d}'

# Time complexity: O(1)
# Space complexity: O(1)



'''
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in. Additionally, if the number is negative, return 0 (for languages that do have them).

Note: If the number is a multiple of both 3 and 5, only count it once.

'''
def solution(number):
    if number <= 0:
        return 0
    total_sum = 0

    for num in range(1, number):
        if num % 3 == 0 or num % 5 == 0:
            total_sum += num

    return total_sum


# Time complexity: O(n)
# Space complexity: O(1)



'''
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

'''
def find_it(seq):
    count_dict = {}

    for num in seq:
        if num not in count_dict:
            count_dict[num] = 1
        else:
            count_dict[num] += 1

    for num, count in count_dict.items():
        if count % 2 == 1:
            return num

# Time complexity: O(n)
# Space complexity: O(n)
