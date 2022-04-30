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

#print(binarySearch(list(range(4500)), 5000))
#print(binarySearchWhileLoop(list(range(4500)), 5000))