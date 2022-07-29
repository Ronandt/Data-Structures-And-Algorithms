def selectionSort( theseq ): #selection sort
    n = len(theseq)
    for i in range(n-1):
        smallnum = i
        for j in range(i+1,n):
            if theseq[j] > theseq[smallnum]:
                smallnum = j
        if smallnum != i:
            tmp = theseq[i]
            theseq[i] = theseq[smallnum]
            theseq[smallnum] = tmp
print("Selection Sort")
list_of_numbers = [12, 7, 9, 24, 7, 29, 5, 3, 11, 7]
print(list_of_numbers)
selectionSort(list_of_numbers)
print(list_of_numbers)


