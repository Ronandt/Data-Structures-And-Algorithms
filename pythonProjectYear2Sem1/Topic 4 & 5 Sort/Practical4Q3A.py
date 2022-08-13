list_of_flowers = ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
list = []
list2 = []
for s in list_of_flowers:
    if s.startswith('H'):
        list.append(s)
    else:
        list2.append(s)
sortedlist2 = sorted(list2)
for s in sortedlist2:
    list.append(s)
print("Unsorted List")
print(list_of_flowers)
print("Sorted List")
print(list)
# def descending(list, ascending =True):
#     return tuple(sorted((list), reverse=ascending))
#
# print(descending(list))