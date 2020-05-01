#Merge sort algroithm

import time

def merge_sort(merge_list):
    #Divide the list into two seperate lists
    if len(merge_list) > 1:
        mid = len(merge_list) // 2
        left_half = merge_list[mid:]
        right_half = merge_list[:mid]

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        #Main sorting loop
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                merge_list[k] = left_half[i]
                i += 1
            else:
                merge_list[k] = right_half[j]
                j += 1
            #End if
            k += 1
        #End while

        #Check for unmerged elements on left half
        while i < len(left_half):
            merge_list[k] = left_half[i]
            i += 1
            k += 1
        #End while

        #Check for unmerged elements on right half
        while j < len(right_half):
            merge_list[k] = right_half[j]
            j += 1
            k += 1
        #End while
    #End if
#End function

merge_list = [6,5,2,77,55,334,53,553,53,64,76,24,86,43,55,1,335,545,6,7,38]
start = time.perf_counter()
merge_sort(merge_list)
end = time.perf_counter()
elapsed = end - start
print("Sorted list: ", merge_list, " Time taken: ", elapsed)
