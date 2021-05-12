def merge_sort(arr):
    '''merge sort splits the array into two and further breaks it and then joins it later'''

    if len(arr) > 1:
        l_arr = arr[:len(arr)//2]
        r_arr = arr[len(arr)//2:]

        merge_sort(l_arr)
        merge_sort(r_arr)

        #merge
        i = 0
        j = 0
        k = 0
        while i < len(l_arr) and j < len(r_arr):    
            if l_arr[i]  < r_arr[j]: 
                arr[k] = l_arr[i]
                i += 1
                
            else:
                arr[k] = r_arr[j]
                j += 1 
            k += 1


        while i < len(l_arr):
            arr[k] = l_arr[i]
            i += 1
            k += 1

        while j < len(r_arr):
            arr[k] = r_arr[j]
            j += 1
            k += 1
#import numpy as np
#np.random.seed(0)
#big_list = np.random.permutation(100)

arr_test = [2,4,5,7,1,9,31,35,15,6,36,13,5,0]
#merge_sort(big_list)
#print(big_list)

import os
os.environ['PATH']