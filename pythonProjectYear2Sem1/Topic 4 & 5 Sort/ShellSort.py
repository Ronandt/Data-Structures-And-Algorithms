# Improvement:
# I used Shell Sort Instead of Insertion Sort
#
# Shell sort is a similar algorithm to insertion sort.
# It sorts the elements that are far apart from one another and successively reduces the interval between the elements to be sorted.
# The interval between the elements is reduced based on the sequence used. The logic of shell sort is to sort entries that are further
# away first. This means that for a partially sorted list, it should be faster than O(n^2) which is the time complexity of insertion sort.
# This means that shell sort is faster on average than insertion sort.
# Shell Sort has a time complexity of O(nlog n) at its best, O(n^2) at its worst and O(nlog n) as its average.

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
      for start_position in range(sublistcount):
        gap_InsertionSort(alist, start_position, sublistcount)

      sublistcount = sublistcount // 2

def gap_InsertionSort(nlist,start,gap):
    for i in range(start+gap,len(nlist),gap):

        current_value = nlist[i]
        position = i


# Test Codes
list_of_numbers = [10,51,2,18,4,31,13,5,23,64,29]
print('Input List:', list_of_numbers)
shellSort(list_of_numbers)
print("Sorted List: ",list_of_numbers)