# LINK: https://www.codewars.com/kata/5ab6538b379d20ad880000ab/train/python
# Resource: https://www.mathsisfun.com/geometry/perimeter.html
def area_or_perimeter(l , w):
    if l == w:
        return l * w
    elif l != w:
        return (l*2) + (w*2)
    
print(area_or_perimeter(3, 6))

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 25.05.2023
# ? == BREADCOWN ======================================================================= DESCRIPTION ====
# ? If l is equal to w, then return Area                                                | IF == --> Area
# ? Else if l is not equal to w, return the Perimeter                                   | ELIF != --> Perimeter