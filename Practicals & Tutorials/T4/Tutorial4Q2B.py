def insertionSort( theseq ):
    n = len(theseq)
    for i in range(1,n):
        value = theseq[i]

        pos = i
        while pos > 0 and value < theseq[pos-1]:
            theseq[pos] = theseq[pos-1]
            pos -=1
        theseq[pos] = value

list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print("InsertionSort")
print(list_of_numbers)
insertionSort(list_of_numbers)
print(list_of_numbers)
