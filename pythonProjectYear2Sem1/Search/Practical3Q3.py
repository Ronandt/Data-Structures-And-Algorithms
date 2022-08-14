def binarySearch( theValues, target ):

    low = 0
    high = len(theValues)-1
    while high>=low:
        mid = (high+low)//2
        print(mid)
        if theValues[mid] == target:
            first_occurence = mid
            cont = True
            while first_occurence >0 and cont:
                if theValues[first_occurence -1] == target:
                    first_occurence -=1
                else:
                    cont = False
            return first_occurence
            # return last_occurence
        elif theValues[mid] < target:
            low = mid+1
        else:
            high = mid- 1
    return -1
list =[0,1,3,3,2,2,2,3,4,5,6,7,8,9,10]
target = 2
search = binarySearch(list,target)
if search == -1:
    print(f"{target} is not in the list")
else:
    print(search)


