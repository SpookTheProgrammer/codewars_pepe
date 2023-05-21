def high_and_low(numbers):
    numbers = numbers.replace(' ', '')
    numbers = list(numbers, '-')
    # for current in numbers:
    #     numbers = current[0]
    return numbers


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))