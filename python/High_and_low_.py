def high_and_low(numbers):
    
    numbers = numbers.split()
    res = [eval(i) for i in numbers]
    maxn = str(max(res))
    minn = str(min(res))
    return f'{maxn} {minn}'
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 21.05.2023
# ? == BREADCOWN ======================================================================================== DESCRIPTION ==
# ? 1. Split each string character with space as a value in an array.                                   | ARRAY
# ? 2. Convert to integers (res)                                                                        | INT
# ? 3. Initialize maximum value within the array as maxn                                                | MAX
# ? 4. Initialize minimum value within the array as minn                                                | MIN
# ? 5. return max and min values                                                                        | f'{var} {var}'