#Dutch flag variant 2:
def dflag():
    a = [1,4,3,2,1,1,4,1,3,4,2]
    N = len(a)
    first = a[0]
    fi = 1 #first index
    for i in range(3):
        for i in range(1,N):
            if a[i] == first:
                a[i],a[fi] = a[fi],a[i]
                fi+=1
        print(fi)
        first = a[fi]
    print(a)
        
#Expected all elements are grouped in place
dflag()