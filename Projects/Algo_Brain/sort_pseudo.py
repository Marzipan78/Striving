def merge_sort(A,p,r):
    if p < r: 
        q = [( p + q)/ 2]
        
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)

def merge(A,p,q,r):
    n1 = q - p + 1
    n2 = r - q

    l = 0  
    l2 = 0

    for i  in  range(1,len(n1)):
        l[i] = A[p + i - 1 ]

    for j in range(1,len(n2)):
        R[j] = A[q + j]
        