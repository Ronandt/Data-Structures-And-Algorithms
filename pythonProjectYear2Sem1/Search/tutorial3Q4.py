

ListNumberElements = [10, 23, 25, 34, 36, 42, 63, 74, 87, 87, 92, 99]


def binary_searchVer2(numlist, target):
    begin_index = 0
    end_index = len(numlist) - 1

    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index)//2
        midpoint_value = numlist[midpoint]
        if midpoint_value == target:
            return midpoint
        elif target < midpoint_value:
            end_index = midpoint - 1
        else:
            begin_index = midpoint + 1
    return None

print(binary_searchVer2(ListNumberElements, 36))

