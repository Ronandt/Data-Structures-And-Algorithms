def sequentialSearch(theValues, target ):
    n = len(theValues)
    for i in range(n):
        # If the target is in the ith element, return True

        if theValues[i] == target:
            return True
    return False

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