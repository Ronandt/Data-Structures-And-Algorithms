
# Python3 program for implementation of Shell Sort
# Python3 program for implementation of Shell Sort
  
def shellSort(arr, n):
    # code here
    gap=n//2
    while gap>0:
        j=gap
        while j<n:
            i=j-gap 
            while i>=0:
                if arr[i+gap]>arr[i]:
                    break
                else:
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]
                i=i-gap 
            j+=1
        gap=gap//2
  
  
  
  
  
# driver to check the code
arr2 = [10,51,2,18,4,31,13,5,23,64,29]
print("input array:",arr2)
  
shellSort(arr2,len(arr2))
print("sorted array",arr2)
  