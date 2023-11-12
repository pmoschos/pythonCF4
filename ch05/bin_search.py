def binary_search(my_array, element, start, end):
    if start > end:
        return -1
    
    mid = (start + end) // 2

    if my_array[mid] == element:
        return mid
    elif my_array[mid] < element:
        return binary_search(my_array, element, mid + 1, end)
    else:
        return binary_search(my_array, element, start, mid - 1)

def main():
    my_array = [1, 2, 3, 4, 5, 6, 7]
    element = 20
    result = binary_search(my_array, element, 0, len(my_array) - 1)
    
    print(f"{element} found in position {result}")

if __name__ == "__main__":
    main()