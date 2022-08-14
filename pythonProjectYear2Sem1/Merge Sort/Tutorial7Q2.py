def mergeSort (thelist, sortorder):
    if len(thelist)<=1:
        return thelist
    else:
        mid = len(thelist)//2

        lefthalf = mergeSort(thelist[:mid],sortorder)
        righthalf = mergeSort(thelist[mid:],sortorder)

        newlist = recquicksort(lefthalf, righthalf, sortorder)

        return newlist

def recquicksort(a,b, sortorder):
    list = []
    if sortorder == "A":
        while len(a) >= 1 and len(b) >= 1:
            if a[0] > b[0]:
                list.append(b[0])
                b.remove(b[0])
            else:
                list.append(a[0])
                a.remove(a[0])

        while len(a) >= 1:
            list.append(a[0])
            a.remove(a[0])

        while len(b) >= 1:
            list.append(b[0])
            b.remove(b[0])
    elif sortorder =="D":
        while len(a) >= 1 and len(b) >= 1:
            if a[0] < b[0]:
                list.append(b[0])
                b.remove(b[0])
            else:
                list.append(a[0])
                a.remove(a[0])

        while len(a) >= 1:
            list.append(a[0])
            a.remove(a[0])

        while len(b) >= 1:
            list.append(b[0])
            b.remove(b[0])

    return list

print(mergeSort([4, 7, 1, 8, 3, 2, 6, 5],"A"), "Ascending")
print(mergeSort([5, 2, 7, 8, 1, 4, 6, 3],"D"), "Descending")
