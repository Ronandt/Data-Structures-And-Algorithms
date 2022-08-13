list1 = []
list2 = []

def arrrec(n):
    if n == []:
        return n
    if int(n[0])%2 == 0:
        list1.append(n[0])
        return arrrec(n[1:])
    else:
        list2.append(n[0])
        return arrrec(n[1:])

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(arrrec(list))
for i in list2:
    list1.append(i)
print(list1)

