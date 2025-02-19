def function_with_uncommon_bug(x):
    if x == 0:
        return 0
    else:
        return 1 / x

# This will raise a ZeroDivisionError, which is common.
# However, the less common bug is that the code doesn't handle other errors like TypeError.
# What if we input a string? 