from typing import List

def triple_step(total_steps:int,valid_jumps:List[int])-> int:
    return trs(total_steps,valid_jumps)

def trs(ts,vj)-> int:
    t = 0
    for j in vj:
        if j<ts:
            t = t + 1 + trs(ts-j,vj)
    return t
    
print(triple_step(9,[1,2]))