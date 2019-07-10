from typing import List

def triple_step(top:int,valid_jumps:List[int])-> int:
    return trs(top,valid_jumps)

def trs(top,vj)-> int:
    t = 0
    exceed = 0
    for j in vj:
        if j == top:
            t+= 1
        elif j<top:
            r = trs(top-j,vj)
            if r >0:
                t +=  r
            else:
                exceed+=1
        else:
            exceed +=1
    if len(vj) == exceed:
        return -1
    return t
    
print(triple_step(4,[1,2]))