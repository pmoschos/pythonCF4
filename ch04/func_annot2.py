def my_add(a: int | float, b: int | float) -> int | float:
    """
    Adds two numbers.

    Args:
        a -- The fisrt number.
        b -- The second number.

    Returns:
        The sume of the two numbers
    """
    return a + b

print(my_add(10.5, 50))