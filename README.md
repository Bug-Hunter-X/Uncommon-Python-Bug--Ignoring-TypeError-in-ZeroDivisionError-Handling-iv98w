# Uncommon Python Bug: Ignoring TypeErrors

This repository demonstrates a subtle bug in Python that's easily missed. The function `function_with_uncommon_bug` is designed to handle `ZeroDivisionError`. However, it fails to gracefully handle other potential errors, such as `TypeError`, that can occur if the function receives unexpected input types. 

The solution demonstrates how to add more robust error handling using a `try-except` block to catch both `ZeroDivisionError` and `TypeError`.
