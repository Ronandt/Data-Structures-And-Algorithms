# Sorts a Python list in ascending order using the merge sort
# algorithm
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
def mergeSortedLists(lista,listb):
    list = []
    a = 0
    b = 0
    while a<len(lista) and b <len(listb):
        if lista[a] < listb[b]:
            list.append(lista[a])
            lista.remove(lista[a])
        else:
            list.append(listb[b])
            listb.remove(listb[b])
    while a<len(lista):
        list.append(lista[a])
        lista.remove(lista[a])
    while b<len(listb):
        list.append(listb[b])
        listb.remove(listb[b])
    return list
list = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print('Input List:', list)
list = mergeSort(list)
print('Sorted List:', list)
