from math import ceil, floor

def round_it(n):
    l, r = [len(x) for x in str(n).split('.')]
    if r > l:
        return ceil(n)
    elif r < l:
        return floor(n)
    else:
        return round(n)
        

print(round_it(3.2233))

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 22.05.2023
# ? == BREADCOWN ==================================================================================================== DESCRIPTION ==
# ? 1. Split the integer with decimal from the . point as two arrays. if the number after the decimal is bigger     | INLINE
# ? --> return ceil(n)                                                                                              | IF r > l => Ceil
# ? 2. Else if the number after the decimal is bigger than the one infron the decimal                               | ELIF r < l
# ? --> return floor(n)                                                                                             | RETURN => Floor
# ? If no other options is available, then just round the integer.                                                  | ELSE => Round