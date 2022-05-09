from AlgorirthmDataPipeline import AlgorithmDataPipeline
import unittest

def bubble_sort(lists):
    
    for _ in range(len(lists)): #n^2
        value = False
        for c in range(len(lists) - 1):
            if AlgorithmDataPipeline.compare(lists[c].lower().strip(), lists[c+1].lower().strip()):
                lists[c + 1], lists[c] = lists[c], lists[c+1]
                value = True #not sorted yet
        if value == False: #if sorted
            return lists

def selection_sort(lists):
    for count in range(len(lists)):
        minimum = count
        for x in range(count, len(lists)):
            if AlgorithmDataPipeline.compare(lists[minimum].lower().strip(), lists[x].lower().strip()):
                minimum = x
        lists[minimum], lists[count] = lists[count], lists[minimum]

    return lists

def insertion_sort(lists):
    for x in range(1, len(lists)):
        count = 0
        while lists[x- count - 1] > lists[x - count] and x-count != 0: #if 0, stop comparing with negative index\
            lists[x- count - 1], lists[x - count] = lists[x - count], lists[x- count - 1]
            count += 1
    return lists
        



            


print(insertion_sort([3,2,1,432,2,5,6,7,43,2,4,2,21,3]))
        




        



class TestBubbleSort(unittest.TestCase):
    def bubble_sort_test(self):
        for _ in range(100):
            sampling = __import__("random").sample("jsfofdfsdiojfsdfds", 6)
            self.assertEqual(bubble_sort(sampling), list(sorted(sampling)))

    def selection_sort_test(self):
        for _ in range(100):
            sampling = __import__("random").sample("jsfofdfsdiojfsdfds", 6)
            self.assertEqual(selection_sort(sampling), list(sorted(sampling)))
          

unittest.main()
       
print(ord("youtube"))
