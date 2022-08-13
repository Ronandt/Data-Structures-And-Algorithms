# Enchancement of Practical4Q3A
# Instead of sorting two list with a for loop and with the 'sorted' command
# I used insertion sort to sort the list of letters as well as sort the letters starting with 'h' first


def insertionSortStartingWithLetterH(theSeq):
    n = len(theSeq)

    # Starts with the first item as the only sorted entry.
    print("Insertion Sort")
    for i in range(1,n):
        #Save the value to be positioned
        value = theSeq[i]

        #Find the position where value fits in the ordered
        #part of the list
        pos = i

        while pos > 0 and value < theSeq[pos-1]:
            #Shift the items to the right during the search
            theSeq[pos] = theSeq[pos-1]
            pos-=1

        #Put the saved valye into the open slot.
        theSeq[pos] = value
        print(f"Pass: {i} {theSeq}")

    print("")
    print('Sort By Letter H')
    posX = 0
    for x in range(0, n):
        value = theSeq[x]

        if value.lower().startswith("h"):
            value2 = theSeq[posX]
            theSeq[posX] = theSeq[x]
            posX += 1

            theSeq[x] = value2

        print(f"Pass: {x} {theSeq}")
    return theSeq


list_of_flowers = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']

print("Unsorted List", list_of_flowers)
print("SortedList", insertionSortStartingWithLetterH(list_of_flowers))


