from random import randint
from timeit import repeat
''' Python implementation of QuickSort using Hoare's  
partition scheme. '''
  
''' This function takes last element as pivot, places  
the pivot element at its correct position in sorted  
    array, and places all smaller (smaller than pivot)  
to left of pivot and all greater elements to right  
of pivot '''

# Driver code  
arr = [6,5,2,77,55,334,53,553,53,64,76,24,86,43,55,1,335,545,6,7,38] 
n = len(arr) 

def partition(arr, low, high): 
      
    pivot = arr[low]  
    i = low - 1
    j = high + 1
      
    while (True): 
          
        # Find leftmost element greater than  
        # or equal to pivot  
        i += 1
        while (arr[i] < pivot): 
            i += 1
              
        # Find rightmost element smaller than  
        # or equal to pivot  
        j -= 1
        while (arr[j] > pivot): 
            j -= 1
              
        # If two pointers met.  
        if (i >= j): 
            return j  
          
        arr[i], arr[j] = arr[j], arr[i] 
      
''' The main function that implements QuickSort  
arr --> Array to be sorted,  
low --> Starting index,  
high --> Ending index '''
def quickSort(arr, low, high): 
  
    ''' pi is partitioning index, arr[p] is now  
    at right place '''
    if (low < high): 
          
        pi = partition(arr, low, high)  
          
        # Separately sort elements before  
        # partition and after partition  
        quickSort(arr, low, pi)  
        quickSort(arr, pi + 1, high)  
          
''' Function to pran array '''
def printArray(arr, n): 
    for i in range(n): 
        print(arr[i],end=" ")  
    print()  


def run_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" \
        if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

    # Finally, display the name of the algorithm and the
    # minimum time it took to run
    print(f"Algorithm: {algorithm}. Minimum execution time: {min(times)}")


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, n) for i in range(n-1)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="quickSort", array=array)
    
quickSort(arr, 0, n - 1)  
print("Sorted array:")  
printArray(arr, n) 
