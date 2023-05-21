def reverseWords(string):
    index = []
    s = ""
    index += string[::-1].split(' ')
    index.reverse()
    for i in index:
        s += i + " "
    return s[:-1]
print(reverseWords("This is Python!"))

# * SUCCESSFULLY COMPLETED WITHOUT UNLOCKING SOLUTION
# * Completed Date: 19.05.2023
# ? == BREADCOWN ======================================================================================== DESCRIPTION ==
# ? 1. Store the reversed string in array (reversed "whole" string)                                     | EMPTY
# ? 2. Store the final array reversed position as string                                                | EMPTY
# ? 3. Reverse the whole string anc each string with a space, create a new array index                  | variable array
# ? 4. Reverse index array                                                                              | variable array
# ? 5. Loop through index array and for each array value add a space. Then store that in new value s    | array to string
# ? 6. return new string from array s and erase the extra space by [:-1]                                | RETURN variable string minus last character