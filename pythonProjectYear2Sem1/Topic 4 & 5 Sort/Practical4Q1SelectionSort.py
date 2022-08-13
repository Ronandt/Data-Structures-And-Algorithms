# Sort a sequence in ascending order using the selection sort
# algorithm
def selectionSort(theSeq):
    n = len(theSeq)
    while True:
        choice = input("Asecending Sort or Descending Sort?(A or D): ")
        if choice.upper() == "A":
            for i in range(n - 1):
                # Assume the ith element is the smallest.
                smallNdx = i
                # Determine if any other element contains a smaller value.
                for j in range(i + 1, n):
                    if theSeq[j] < theSeq[smallNdx]:
                        smallNdx = j
                # Swap the ith value and smallNdx value only if the smallest value
                # is not already in its proper position
                if smallNdx != i:
                    tmp = theSeq[i]
                    theSeq[i] = theSeq[smallNdx]
                    theSeq[smallNdx] = tmp
            return theSeq
        if choice.upper() == "D":
            for i in range(n - 1):
                # Assume the ith element is the smallest.
                smallNdx = i
                # Determine if any other element contains a smaller value.
                for j in range(i + 1, n):
                    if theSeq[j] > theSeq[smallNdx]:
                        smallNdx = j
                # Swap the ith value and smallNdx value only if the smallest value
                # is not already in its proper position
                if smallNdx != i:
                    tmp = theSeq[i]
                    theSeq[i] = theSeq[smallNdx]
                    theSeq[smallNdx] = tmp
            return theSeq
        else:
            print("Please Enter A or D only!")






# Test Codes
list_of_numbers = [10,51,2,18,4,31,13,5,23,64,29]

print(f"Input List: ",list_of_numbers)
selectionSort(list_of_numbers)
print("Sorted List: ",list_of_numbers)

