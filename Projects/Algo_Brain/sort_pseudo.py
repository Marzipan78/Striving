def merge_sorta(A,p,r):
    if p < r:
        q = [(p+q)/2]
        merge_sorta(A,p,q)
        merge_sorta(A,q+1,r)

def merge(A,p,q,r):
    n1 = q-p + 1
    n2 = r - q

    l = 0
    l1 = 0 

    for i in n1:
        l[i] = A[p + i - 1]
        
