Name: Tan Ch'ing Jui Benjamin
Admin Number: 210733T
Module Group: IT2153

My Advance Features
================================================================================================================================================
Week 3
Practical 3 Q3 Binary Search
Filename: ExponentialSearch.py
Improvement:
I used exponential search instead of Binary Search

Exponential Search works in two steps, first is to find the range where the element is present
and then do a binary search in the above found range. Its time complexity O(Log n). Exponential search
works better than Binary Search for bounded arrays and also when the element to be searched is close to the first element.
Exponential Binary search is also particularly useful for unbounded searches where the size of the array is infinite.
Exponential Search starts with a subarray size of 1, compare last element with x, then try size 2, then 4 until the
last subarray is not greater. Once finding the index, we can conclude that the element will be present between i/2 and i.
As exponential search is very similar to binary with the only difference being finding the range where the element falls in between
the list hence it was only mildly difficult to implement.

================================================================================================================================================
Topic 4 & 5 Sort
Practical 4 Q1 SelectionSort
Filename: Heap Sort.py
Improvement:
I used heap sort instead of Selection sort

Heapsort is a comparison based sorting technique based on a Binary Heap data structure.
It is similar to selection sort where we first find the maximum element and place the maximum element at the end.
We repeat the same process for the remaining element.

Time Complexity: O(n*log(n))
================================================================================================================================================
Topic 4 & 5 Sort
Practical 4 Q2 InsertionSort
Filename: ShellSort.py
Improvement:
I used Shell Sort Instead of Insertion Sort

Shell sort is a similar algorithm to insertion sort.
It sorts the elements that are far apart from one another and successively reduces the interval between the elements to be sorted.
The interval between the elements is reduced based on the sequence used. The logic of shell sort is to sort entries that are further
away first. This means that for a partially sorted list, it should be faster than O(n^2) which is the time complexity of insertion sort.
This means that shell sort is faster on average than insertion sort.
Shell Sort has a time complexity of O(nlog n) at its best, O(n^2) at its worst and O(nlog n) as its average.

Time Complexity:
Best: O(nlog n)
Average: O(nlog n)
Worst: O(n^2)
================================================================================================================================================
Topic 4 & 5 Sort
Practical 4 Q3A
Filename: Practical4Q3AEnhancement.py
Improvement:
I used insertion sort to help sort the list as well as to help put letters starting with the letter 'H' first.
Another small improvement is checking for both lower case 'h' and uppercase 'H'

In the original program the list ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
was sorted to ['Hibiscus', 'Honeysuckle', 'Bougainvillea', 'Frangipani', 'Orchids']
by making 2 lists sorting each of them and then combining them.

In the original code this was done in simple ways such as by using a for loop to add words starting with the letter H in one list,
and adding the others words in another list and then combining the two lists once sorted. I thought the original code was quite simple as to
sort the list the built-in command of 'sorted' could be used to sort the list also the code was a little messy and I wanted to be able to sort
the two lists another way.

For my improvement I thought it would be interesting to sort my list with insertion sort instead. I would firstly use insertion sort to sort
the entire list alphabetically. After that was done my code would then check for words starting with the letter 'h' and just like insertion sort
once it finds a letter starting with the letter h it swaps with the first index 0 and then if it finds another letter starting with 'h' it would
swap with the 2nd index that being index 1.

I thought this would make the function stable as well as all indexes in the list retain their original order.

Sample Output:
Unsorted List ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
Insertion Sort
Pass: 1 ['Bougainvillea', 'Orchids', 'Hibiscus', 'Frangipani', 'Honeysuckle']
Pass: 2 ['Bougainvillea', 'Hibiscus', 'Orchids', 'Frangipani', 'Honeysuckle']
Pass: 3 ['Bougainvillea', 'Frangipani', 'Hibiscus', 'Orchids', 'Honeysuckle']
Pass: 4 ['Bougainvillea', 'Frangipani', 'Hibiscus', 'Honeysuckle', 'Orchids']

Sort By Letter H
Pass: 0 ['Bougainvillea', 'Frangipani', 'Hibiscus', 'Honeysuckle', 'Orchids']
Pass: 1 ['Bougainvillea', 'Frangipani', 'Hibiscus', 'Honeysuckle', 'Orchids']
Pass: 2 ['Hibiscus', 'Frangipani', 'Bougainvillea', 'Honeysuckle', 'Orchids']
Pass: 3 ['Hibiscus', 'Honeysuckle', 'Bougainvillea', 'Frangipani', 'Orchids']
Pass: 4 ['Hibiscus', 'Honeysuckle', 'Bougainvillea', 'Frangipani', 'Orchids']
SortedList ['Hibiscus', 'Honeysuckle', 'Bougainvillea', 'Frangipani', 'Orchids']


================================================================================================================================================
Topic 6 Recursion
Tutorial 6 Q4
Filename: ReverseFunctionPalindromeChecker.py
Is it a Palindrome?

Improvement:
Checking If String is a Palindrome with a reverse Function

Python enables us to use the reverse function. We know intuitively that a word read forwards and backwards, if same is a palindrome.
Hence, let us generate the forward and backward string for the same, and check if the two strings are the same.

Link:https://www.mygreatlearning.com/blog/palindrome-in-python/#reverse-function
================================================================================================================================================
Topic 10 Stacks
Practical10Q2
Filename: Practical10Q2.py
Postfix Expression Evaluator

Improvement:
Allows addition of sin and cos numbers for the postfix expression evaluation
e.g
input - > 5 6 sin+
math -> sin(5) + sin(6) - Degree mode for your calculator
output -> 0.19168420601531164

Link: https://www.w3schools.com/python/ref_math_sin.asp
Link on Math Library on math.sin()
================================================================================================================================================