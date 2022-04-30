from AlgorirthmDataPipeline import AlgorithmDataPipeline
import unittest

def bubble_sort(lists):
    
    for _ in range(len(lists)):
        value = False
        for c in range(len(lists) - 1):
            if AlgorithmDataPipeline.compare(lists[c].lower().strip(), lists[c+1].lower().strip()):
                lists[c + 1], lists[c] = lists[c], lists[c+1]
                value = True
        if value == False:
            return lists

def selection_sort(lists):
    for count in range(len(lists)):
        minimum = count
        for x in range(count, len(lists)):
            if AlgorithmDataPipeline.compare(lists[minimum], lists[x]):
                minimum = x
        lists[minimum], lists[count] = lists[count], lists[minimum]

    return lists

def insertion_sort(lists):
    previous = 0
    for x in range(len(lists)):
        count = 0
        while lists[previous - count] > lists[x - count]:
            lists[previous - count], lists[x - count] = lists[x - count], lists[previous - count]
            count += 1
    return lists
        



            


print(insertion_sort([3,2,1]))
        




        



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
