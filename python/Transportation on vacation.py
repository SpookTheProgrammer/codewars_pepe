def rental_car_cost(d):
    if 3 <= d < 7:
        return (d * 40) - 20
    elif d >= 7:
        return (d * 40) - 50
    else:
        return d * 40
        
# https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python

print(rental_car_cost(7))

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 24.05.2023
# ? == BREADCOWN ======================================================================================== DESCRIPTION ==
# ? 1. If days rented for each week is 3 --> Multiply original price with days rented, take result - 20 | IF 3 FOR EACH 7
# ? 2. Else, if the car is rented for a week --> ==''==, take result - 50                               | IF 7 (WEEK)
# ? 3. If no other requirement is met, then return days rented * original price                         | ELSE d * 40