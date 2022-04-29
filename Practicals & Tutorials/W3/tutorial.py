def binarySearch(sortedList : list, target: int) -> bool:
    if sortedList == []: return False
    current = sortedList[(len(sortedList) -1)//2]
    if current == target: return True
    return  binarySearch(sortedList[sortedList.index(current) + 1: len(sortedList)], target) if target>current else binarySearch(sortedList[:sortedList.index(current)], target)
    

def binarySearchWhileLoop(sortedList: list, target: int) -> bool:
    current = sortedList[(len(sortedList) - 1)// 2]
    while sortedList != []:
        if target > current:
            sortedList = sortedList[((len(sortedList) - 1)// 2) + 1:]
        elif target < current:
            sortedList = sortedList[:((len(sortedList) - 1)// 2)]
        else:
            return True
    return False

        
        
        
        


print(binarySearch(list(range(4500)), 5000))
print(binarySearchWhileLoop(list(range(4500)), 5000))