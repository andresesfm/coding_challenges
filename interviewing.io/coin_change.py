def num_coins(cents: int) -> int:
    vals = [25,10,5,1]
    currval = cents
    coins = 0
    for c in vals:
        d = currval // c
        if d >0:
            coins +=d
            currval -= d * c 
        
    return coins

print(num_coins(31))
#first pass at dynamic programming answer general case
def num_coins2(cents:int)-> int:
    vals = [25,10,1]
    scounters = [0,0,0]
    memo = {}
    currentVal = 0
    MAX_VAL = 1000000
    def value(counters) -> int:
        v = 0
        for c in range(len(vals)):
            v += vals[c]* counters[c]
        return v
    def helper(counters,rcents:int)-> int:
        if cents <=0:
            return 0
        v = value(counters)
        if v>cents:
            return MAX_VAL
        if  v == cents:
            return sum([i for i in counters])
        m = MAX_VAL
        for i in range(len(counters)):
            cm = helper([y+1 if x == i else y for x,y in enumerate(counters)],rcents-vals[i])
            if cm < m:
                m = cm
        return m
    return helper(scounters,cents)

print(num_coins2(31),'coins')