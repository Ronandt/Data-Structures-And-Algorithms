# Sorts a sequence in ascending order using the
# optimized bubble sort algorithm
def bubbleSort_optimized(theSeq):
    n = len(theSeq)
# Perform n-1 bubble operations on the sequence
    for i in range(n - 1, 0, -1):
        noswap = True
        # Set boolean variable to check occurrence of swapping
        # in inner loop
        # Bubble the largest item to the end
        for j in range(i):
            if theSeq[j] > theSeq[j + 1]:
            # Swap the j and j+1 items
                tmp = theSeq[j]
                theSeq[j] = theSeq[j + 1]
                theSeq[j + 1] = tmp
                noswap = False

        if noswap:
            break

# Set boolean variable value if swapping occurre

# Exit the loop if no swapping occurred
# in the previous pass
list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
print("Bubble Sort")
print(list_of_numbers)
bubbleSort_optimized(list_of_numbers)
print(list_of_numbers)

