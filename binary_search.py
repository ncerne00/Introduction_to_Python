def binary_search(values, target):
    low = 0
    high = len(values) - 1
    mid = 0

    while high >= low:
        mid = (low + high) // 2

        if target == values[mid]:  # target was found
            return mid
        elif target < values[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # target is not in list