#Handles sorted list ascending
def sortedSequentialSearch( theValues, target ):
    n = len(theValues)
    for i in range(n):
        if theValues[i] == target:
            return True
        elif theValues[i] > target:
            return False
    return False

print(sortedSequentialSearch([1,2,3,4,5,6,7,8],6))


#handles sorted numbers including both ascending and desending
def ascending(theValues, ascending= True):
        return tuple(sorted((theValues), reverse=ascending))
def sortedSequentialSearch( theValues, target ):
    n = len(theValues)
    print(ascending((theValues)))
    print(theValues)
    if theValues.sort() == ascending(theValues):
        for i in range(n):
            if theValues[i] == target:
                return True
            elif theValues[i] < target:
                return False
        return False
    else:
        for i in range(n):
            if theValues[i] == target:
                return True
            elif theValues[i] > target:
                return False
        return False

print(sortedSequentialSearch([1,2,3,4,5,6,7,8,9],6))
print(sortedSequentialSearch([8,7,6,5,4,3,2,1],4))


def findFirstOccurrence(nums, target):
 
    # search space is nums[left…right]
    (left, right) = (0, len(nums) - 1)
 
    # initialize the result by -1
    result = -1
 
    # loop till the search space is exhausted
    while left <= right:
 
        # find the mid-value in the search space and compares it with the target
        mid = (left + right) // 2
 
        # if the target is located, update the result and
        # search towards the left (lower indices)
        if target == nums[mid]:
            result = mid
            right = mid - 1
 
        # if the target is less than the middle element, discard the right half
        elif target < nums[mid]:
            right = mid - 1
 
        # if the target is more than the middle element, discard the left half
        else:
            left = mid + 1
 
    # return the leftmost index, or -1 if the element is not found
    return result
 

def binryOne(sortedList: list, target: int, pointer1 , pointer2) -> bool:

 
    
    if pointer2 >= pointer1:
        mid = (pointer1 + pointer2 )//2 #assuming simply taking the length
        print(mid)

      
        if sortedList[mid] == target:
            return True
        elif sortedList[mid] > target:
            return binryOne(sortedList, target, pointer1, mid - 1)
        else:
            return binryOne(sortedList, target, mid + 1, pointer2)
    else:
        print("f")
        return False


        
        
lists = list(range(3))      
print(binryOne(lists, 2, 0, len(lists) - 1))

