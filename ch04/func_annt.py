def my_add(a: int, b: int) -> int:
    """
    Adds two integers.

    Args:
        a (int) -- The fisrt integer.
        b (int) -- The second integer.

    Returns:
        int: The sume of the two integers
    """
    return a + b

print("10 + 20", my_add(10, 20))
print("Annotations:", my_add.__annotations__)
print("Doc:", my_add.__doc__)

help(my_add)