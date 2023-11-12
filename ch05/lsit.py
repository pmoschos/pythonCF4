def get_reversed(arr):
    """
    Prints the reversed string
    """
    if arr == None:
        return []
    return arr[::-1]

print(f"{get_reversed("Coding Factory")}")