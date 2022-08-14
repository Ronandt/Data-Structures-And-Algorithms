# A recursive implementation of Binary Search
def recBinarySearch( target, theValues, first, last ):
        # If the sequence of values cannot be subdivided further,
        # we are done
        if last<first: # BASE CASE #1
            return False
        else:
            # Find the midpoint of the sequence
            mid = (first + last)//2
            # Does the element at the midpoint contain the target?
            if theValues[mid] == target:
                return True # BASE CASE #2
            # or does the target precede the element at the midpoint?
            elif target < theValues[mid]:
                return recBinarySearch(target, theValues,first, mid-1 )
            # or does the target follows the element at the midpoint?
            else:
                return recBinarySearch(target, theValues,mid+1, last )

list = [1,2,3,4,5,6,7]
print(recBinarySearch(2, list, 0, len(list)-1))
