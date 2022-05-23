# Function to do insertion sort
def insertionSort(arr):
 
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
 
        key = arr[i]
 
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
                print(arr)
        print(arr)
        arr[j + 1] = key
 
 
# Driver code to test above
arr = [12, 11, 13, 11, 6]
insertionSort(arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
 
# This code is contributed by Mohit Kumra

def insert(arr):
    for i in range(1,len(arr)):
        while arr[i-1] > arr[i] and i > 0:
            arr[i], arr[i-1] = arr[i-1], arr[i]
            i -= 1 
            print(arr)
        print(arr)
    return arr 

arr = [23, 55, 12, 99, 66, 33]
print(insert(arr))