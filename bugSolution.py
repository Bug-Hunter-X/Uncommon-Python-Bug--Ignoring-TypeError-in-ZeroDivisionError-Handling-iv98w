def function_with_uncommon_bug_solution(x):
    try:
        if x == 0:
            return 0
        else:
            return 1 / x
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  # Or handle appropriately
    except TypeError:
        print("Error: Invalid input type. Please provide a number.")
        return None  # Or handle appropriately

#Testing the solution
print(function_with_uncommon_bug_solution(0))
print(function_with_uncommon_bug_solution(10))
print(function_with_uncommon_bug_solution("hello"))
print(function_with_uncommon_bug_solution(5.5))