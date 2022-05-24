def binarySearchRecursi(arr, x, left, right):
    if right <= left:
        return -1
    mid = (left + right) // 2
    if arr[mid] == x:
        return mid
    elif x < arr[mid]:
        return binarySearchRecursi(arr, x, left, mid)
    else:
        return binarySearchRecursi(arr, x, mid + 1, right)


arr = [0, 2, 3, 5, 7, 9, 10, 21]
print(binarySearchRecursi(arr, 3, 0, len(arr)))