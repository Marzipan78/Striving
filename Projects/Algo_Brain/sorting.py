import numpy as np

def merge_sort(arr):
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2]
        right_arr = arr[len(arr)//2:]

        merge_sort(left_arr)
        merge_sort(right_arr)

        #merge
        i=0
        j=0

        while i < len(left_arr) and j < len(right_arr):    
            if left_arr[i]  < right_arr[j]:
                arr[k] = left_arr[i]
                i += 1
                
            else:
                arr[k] = right_arr[j]
                j += 1 
            k += 1