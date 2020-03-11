#Dutch flag variant 13:
def dflag():
    a = [True,False,True, False, False, True]
    N = len(a)
    fi=0
    for i in range(N):
        if a[i] == False:
            a[i],a[fi] = a[fi],a[i]
            fi+=1

    print(a)
        
#Expected all elements are grouped in place
dflag()