# LINK: https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

def array_diff(a, b):
    # SKTECH
    # 1. a is the main array and b is the determining remover from a's array
    # 2. loop through a array
    #   - if the value inside the array equals to the index value of b
            # --> remove that value from a array and return a
    # for i in b:
    #     if i in a:
    #         for s in range(a.count(i)):
    #             a.remove(i)
    #     return a
    return [x for x in a if x not in b]
print(array_diff([1,2,2,2,3],[3])) # [1, 2, 2, 2]

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 26.05.2023
# ? == BREADCOWN ======================================================================================== DESCRIPTION ====
# ? 1. return x through loop a if x is not in b --> check that b is the same as value in a,             | INLINE FOR LOOP
# ? remove and output x as new a without b value                                                        | RETURN NEW X ARRAY