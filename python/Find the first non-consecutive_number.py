def first_non_consecutive(arr):
    for i, j in enumerate(arr, arr[0]):
        if i!=j:
            return j
        
# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 23.05.2023
# ? == BREADCOWN ======================================================================================== DESCRIPTION ======================
# ? 1. Enumerate i as iterable and j as start position arr[0] (gradually goes through each arr value    | ENUMERATE, i, j
# ? 2. i will be equal to 1 and also j will equal to one since the first index position is 1            | ENUMERATE iterable, index position
# ? 3. Check when i is not the same as j in the enumerate list                                          | IF i is not j
# ? 4. Return j when 3.                                                                                 | RETURN j
print(first_non_consecutive([1,2,3,4,6,7,8])) # 6s
print(first_non_consecutive([1,2,3,4,5,6,7,8])) # None