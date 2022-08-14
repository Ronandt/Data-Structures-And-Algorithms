

========================================================================================================================================================
Python overview
Practical 1 Q1/2 CreditCard
Filename: Practical1Q2Property.py/ Practical1Q1Property.py
Improvement: Utilitsed @property instead of formal getter setters

@Property is the proper way to have getters and setters in python and the most pythonic and proper way to do it in python
It is used to give "special" functionality to certain methods to make them act as getters, setters, or deleters when we define properties in a class.
The decorator pattern (@property) is a pythonic way and it is used throughout libraries as getter setter ways

==================================================================================================================================================
================================================================================================================================================
Search
Practical 3 Q3 Binary Search
Filename: ExponentialSearch.py
Improvement:
I used exponential search opposed to binary search

Exponential Search works in two steps: first, it determines the range in which the element exists, and then it performs a binary search within that range. Its time complication O (Log n). For bounded arrays and when the element to be searched is close to the first element, exponential search outperforms binary search.
Exponential Binary search is also useful for unbounded searches where the array size is infinite.
Exponential Search begins with a subarray size of one, compares the last element to x, and then tries size two, then 4 until the last subarray is not greater than the first. We can conclude that the element will be present between i/2 and I after finding the index.
Because exponential search is very similar to binary search, with the only difference being determining the range in which the element falls between the lists,

================================================================================================================================================
Sort
Practical 4 Q1 (bubble sort)
Filename: Combsort.py
Improvement: Used comb sort instead of bubble sort

Comb sort is an algorithm that utilises “gaps” similar to Shell sort which similarly, 
eliminates the issue of “turtles” like Cocktail shaker sort as it is able to swap between first and last elements. 
Consider the array [5, 5, 5, 5, 1] again. Comb sort would be able to swap the first and last element, 
effectively needing one pass to sort. Although, one downside is that the criteria for finishing the sort is having a sorted list. 
This means that the gap needs to be 1 in the first place in order to verify that a list has been sorted.
The most effective “gap” for sorting arrays is a shrink factor of 1.3. Initially,
the gap would be the length of the array, but for every pass of the array, 
the gap would shrink by approximately 1.3. The shrink factor is essential to the run-time complexity of the algorithm.
If the shrink factor is too small, it may cause an unnecessary number of passes. If the shrink factor is too large, 
it may not effectively deal with the issue of “turtles” as the gaps would quickly become small. 
It is commonly used as an educational tool to encourage algorithmic thinking.



===================================================================================================================================================
Sort
Practical 4 Q1 Selection Sort
Filename: Heap Sort.py
Improvement:
I used heap sort instead of selection sort (Better selection sort as it acts as a heap instead of an  array)

Heapsort is a sorting technique that uses comparisons and is based on the Binary Heap data structure.
It is similar to selection sort in that we find the maximum element first and then place it at the end.
We repeat the process for the final element.

Time Complexity: O(n*log(n))
================================================================================================================================================
Sort
Practical 4 Q2 Shell Sort
Filename: ShellSort.py
Improvement:
I used Shell Sort as opposed to Insertion Sort

Shell sort is a similar algorithm to insertion sort.
Shell sort optimises insertion sort by utilising gaps, similar to how Comb sort optimises bubble sort by utilising gaps, 
shrinking at every pass. The basis of shell sort is to reduce the number of exchanges and comparisons between numbers.
 This means its more efficient than insertion sort as it skips the in-between elements

Time Complexity:
Best: O(nlog n) (Depends on gap sequence)
Average: O(nlog n)(Depends on gap sequence)
Worst: O(n^2)(Depends on gap sequence)


================================================================================================================================================
Advanced sort
Filename: InPlaceMergeSort.py

Improvement:
Turning merge sort which has a space complexity of O(n) to O(1). This can take up less memory 

Using in place merge sort would be fast and take up less space. This is especially useful for large datasets and usage of data warehouses.
The in-place merge sort utilises recursion and uses indexes instead of creating a new array.  

================================================================================================================================================
 10 Stacks
Practical10Q2
Filename: Practical10Q2Enhancement.py
Improvement: Instead of the user being able to enter a postfix expression, the user is able to enter infix and the system is able to parse it
(ADDED SHUNTING YARD ALGO)

It is more intuitive and practical for the user to enter infix expressions and the system uses Shunting yard algorithm to convert infix to postfix. Then uses the Stack
(Pop etc) to calculate the translated postfix expression. Hence, this would be a pure mathematical/arithmaticalparser. This type of parsing from infix to postfix
is typically used in compilers to parse the code itself (turning it into an Abstract Syntax Tree) so be further compiled. It is also used in calculators
to evaluate mathematical expressions. Shunting yard algorithm is stack based and uses operations such as adding, pushing, and popping tokens to convert infix 
to postfix 

Time complexity for shunting yard: O(n) (Average, best, worst)

======================================================================================================