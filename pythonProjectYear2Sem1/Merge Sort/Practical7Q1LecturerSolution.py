def mergeSort(theList):
    # Check the base case - the list contains a single item
    if len(theList) <= 1:
        return theList
    else: #Compute the midpoint
        mid = len(theList) // 2
        # Split the list and perform the recursive step
        leftHalf = mergeSort(theList[:mid])
        rightHalf = mergeSort(theList[mid:])
        # Merge the two sorted sublists
        newList = mergeSortedLists(leftHalf, rightHalf)
        return newList

def mergeSortedLists(listA,listB):
    # Create the new list and initiate the list markers
    print("merging the 2 lists")
    print("listA is", listA)
    print("listB is", listB)
    newList = list()
    a = 0
    b = 0

    # Merge the two lists togther until one is empty
    while a < len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            newList.append(listA[a])
            a+=1
        else:
            newList.append(listB[b])
            b+=1

    # If listA contains more items, append remaining items to newList
    while a < len(listA):
        newList.append(listA[a])
        a+=1

    # If listB contains more items, append remaining items to newList
    while b< len(listB):
        newList.append(listB[b])
        b+=1
    return  newList

# Test Code
list_of_numbers = [12,7,9,6,29,5,3,11,21]

print("Input List:", list_of_numbers)
merge_list = mergeSort(list_of_numbers)
print("Sorted List: ", merge_list)

