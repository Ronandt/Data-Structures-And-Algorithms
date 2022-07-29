#Handles sorted list ascending
def sortedSequentialSearch( val, target ):
    n = len(val)
    for i in range(n):
        if val[i] == target:
            return True
        elif val[i] > target:
            return False
    return False

print(sortedSequentialSearch([1,2,3,4,5,6,7,8],6))


#sort numbers obth descending and ascending

def sortedSequentialSearch( val, target ):
    n = len(val)
    if list(sorted(val)) == list(sorted((val), reverse=True)):
        for x in range(n):
            if val[x] == target:
                return True
            elif val[x] < target:
                return False
        return False
    else:
        for i in range(n):
            if val[i] == target:
                return True
            elif val[i] > target:
                return False
        return False

print(sortedSequentialSearch([1,2,3,4,5,6,7,8,9],6))
print(sortedSequentialSearch([8,7,6,5,4,3,2,1],4))


def binarySearch(nums, target):
    (left, right) = (0, len(nums) - 1)
    # initialize the result by -1
    result = -1
    # loop till the search space is exhausted
    while left <= right:
 

        mid = (left + right) // 2

        if target == nums[mid]:
            result = mid
            right = mid - 1
        elif target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return result
 

#recrusive binary search
def binaryOne(sortedList: list, target: int, pointer1 , pointer2) -> bool:

 
    
    if pointer2 >= pointer1:
        mid = (pointer1 + pointer2 )//2 #assuming simply taking the length
        print(mid)

      
        if sortedList[mid] == target:
            return True
        elif sortedList[mid] > target:
            return binaryOne(sortedList, target, pointer1, mid - 1)
        else:
            return binaryOne(sortedList, target, mid + 1, pointer2)
    else:
        print("f")
        return False


        
        
lists = list(range(3))      
print(binaryOne(lists, 2, 0, len(lists) - 1))

