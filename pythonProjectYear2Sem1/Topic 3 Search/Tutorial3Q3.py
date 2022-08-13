
ListNumberElements = [10, 23, 25, 34, 36, 42, 63, 74, 87, 87, 92, 99]


def binary_search(ListNumber,targetNum):
    if len(ListNumber) == 0 and type(ListNumber) != list: return False

    currentNumber = __import__("math").ceil((len(ListNumber)-1)/2)

    check = ListNumber[currentNumber]

    if check == targetNum:
        return ListNumber.index(check)
    else:
        try:
            return binary_search(ListNumber[ListNumber.index(check)+1:len(ListNumber)],targetNum) if targetNum > check else binary_search(ListNumber[:ListNumber.index(check)], targetNum)
        except IndexError:
            return f"Full Binary Search Conducted Target Number does not appear to be in the list"

        except:
            return "Unknown Error"


print(binary_search(ListNumberElements,63))

#

