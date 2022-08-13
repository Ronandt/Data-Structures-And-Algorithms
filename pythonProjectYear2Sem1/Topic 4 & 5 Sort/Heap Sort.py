# Improvement:
# I used heap sort instead of selection sort
#
# Heapsort is a comparison based sorting technique based on a Binary Heap data structure.
# It is similar to selection sort where we first find the maximum element and place the maximum element at the end.
# We repeat the same process for the remaining element.
#
# Time Complexity: O(n*log(n))

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2


    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]


        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)


    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)


    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

list_of_numbers = [10,51,2,18,4,31,13,5,23,64,29]

print(f"Input List: ",list_of_numbers)
heapSort(list_of_numbers)
print("Sorted List: ",list_of_numbers)