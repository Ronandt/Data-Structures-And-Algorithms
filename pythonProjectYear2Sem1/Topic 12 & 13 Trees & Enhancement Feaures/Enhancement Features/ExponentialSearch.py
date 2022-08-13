

def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        if arr[mid] == x:
            return mid


        if arr[mid] > x:
            return binarySearch(arr, l,
                                mid - 1, x)

        return binarySearch(arr, mid + 1, r, x)

    return -1

def exponentialSearch(arr, n, x):
    if arr[0] == x:
        return 0
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2
    return binarySearch(arr, i // 2,
                        min(i, n - 1), x)

# Test Code
ListNumberElements = [10, 23, 25, 34, 36, 42, 63, 74, 87, 87, 92, 99]
target_num = 63
print("Input List:",ListNumberElements)
print("Target Number is:",target_num)
x = exponentialSearch(ListNumberElements,len(ListNumberElements),target_num)
if x != -1:
    print(f"{target_num} found at index {x}")
else:
    print("Target Number was not Found")

