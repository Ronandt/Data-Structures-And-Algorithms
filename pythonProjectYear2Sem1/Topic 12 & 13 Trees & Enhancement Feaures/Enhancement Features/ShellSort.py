

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