from heapq import heappop, heappush
"""
From https://www.youtube.com/watch?v=ztyCQjiAAdU
"""
def thirdSmallest(candidates:set)-> int:
    # Naive: convert to array, sort and get [2]
    # return sorted(candidates,reverse=True)[2] 
    # N log N
    h = []
    for e in candidates:
        heappush(h,-e)
        if len(h)>3:
            heappop(h)
    if len(h)==3:
        return -h[0]
    else:
        return None
        

print(thirdSmallest({1,2,3,4,5,6,7}))

print(thirdSmallest({7,6,5,4,3,2,1}))

print(thirdSmallest({9,1,2,5,6,7}))