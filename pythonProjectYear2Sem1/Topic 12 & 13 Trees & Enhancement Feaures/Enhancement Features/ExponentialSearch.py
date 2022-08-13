# Improvement:
# I used exponential search instead of Binary Search
#
# Exponential Search works in two steps, first is to find the range where the element is present
# and then do a binary search in the above found range. Its time complexity O(Log n). Exponential search
# works better than Binary Search for bounded arrays and also when the element to be searched is close to the first element.
# Exponential Binary search is also particularly useful for unbounded searches where the size of the array is infinite.
# Exponential Search starts with a subarray size of 1, compare last element with x, then try size 2, then 4 until the
# last subarray is not greater. Once finding the index, we can conclude that the element will be present between i/2 and i.
# As exponential search is very similar to binary with the only difference being finding the range where the element falls in between
# the list hence it was only mildly difficult to implement.


def binarySearch(arr, l, r, x):
    if r >= l:
        mid = l + (r - l) // 2

        # If the element is present at
        # the middle itself
        if arr[mid] == x:
            return mid

        # If the element is smaller than mid,
        # then it can only be present in the
        # left subarray
        if arr[mid] > x:
            return binarySearch(arr, l,
                                mid - 1, x)

        # Else he element can only be
        # present in the right
        return binarySearch(arr, mid + 1, r, x)

    # We reach here if the element is not present
    return -1


# Returns the position of first
# occurrence of x in array
def exponentialSearch(arr, n, x):
    # IF x is present at first
    # location itself
    if arr[0] == x:
        return 0

    # Find range for binary search
    # j by repeated doubling
    i = 1
    while i < n and arr[i] <= x:
        i = i * 2

    # Call binary search for the found range
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

