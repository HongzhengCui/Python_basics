def power(x, y):
    # Base case: If y is 0, any number raised to the power of 0 is 1.
    if y == 0:
        return 1
    else:
        # Recursive case: Calculate x raised to the power of (y-1) and multiply it by x.
        # This effectively reduces the problem by decreasing y by 1 in each recursion until y becomes 0.
        return x * power(x, y - 1)
