def recRearrange(orgList, low, high):
    if low < high:
        if orgList[high] % 2 == 0:
            orgList[low],orgList[high] = orgList[high], orgList[low]
            recRearrange(orgList, low + 1, high)
        else:
            recRearrange(orgList, low, high-1)
    else:
        return print(orgList)

originalList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
recRearrange(originalList, 0, len(originalList) -1)