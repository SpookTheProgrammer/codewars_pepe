def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    pos = sum([1 for i in arr if i > 0]) # counts how many positive numbers in the array
    neg = sum([i for i in arr if i < 0]) # sums all the negative numbers
    return  [pos, neg]

print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]))

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 22.05.2023
# ? == BREADCOWN ======================================================================================== DESCRIPTION ==
# ? 1. If the there is no value in the array, return empty array.                                       | CONDITION
# ? 2. Count how many positive numbers in the array                                                     | SUM COUNT
# ? 3. Sums all the negative numbers                                                                    | SUM NEGATIVE INT