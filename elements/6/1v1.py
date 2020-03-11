#Dutch flag variant 1:
def dflag():
    a = [1,3,2,1,3,2]
    N = len(a)
    first = a[0]
    fi = 1 #first index
    for i in range(1,N):
        if a[i] == first:
            a[i],a[fi] = a[fi],a[i]
            fi+=1
    last = a[N-1]
    li = N-2
    for i in range(N-2,-1,-1):
        if a[i] == last:
            a[i],a[li] = a[li],a[i]
            li-=1
    print(a)
        
#Expected all elements are grouped in place
dflag()