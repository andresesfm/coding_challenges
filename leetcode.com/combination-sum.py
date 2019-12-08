from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)
        candidates = sorted(candidates)
        DP=[[[] for j in range(l+1)] for i in range(target+1)]
        for i in range(target+1):
            DP[i][0] = None
        for i in range(1,target+1):
            for j in range(1,l+1):
                allEmpty = True
                for k in range(j,-1,-1):
                    if candidates[k-1] <= i:
                        prev = DP[i-candidates[k-1]][j]
                        if prev == None:
                            continue
                        elif prev == []:
                            DP[i][j].append([candidates[k-1]])
                            allEmpty = False
                        else:
                            for a in prev:
                                na = a[:]
                                na.append(candidates[k-1])
                                DP[i][j].append(na)
                                allEmpty = False
                    else:
                        break
                if allEmpty:
                        DP[i][j] = None
        for e in DP:
            print(e)
        res = set()
        for i in range(1,l+1):
            e = DP[target][i] if DP[target][i] != None else [] 
            for j in e:
                res.add(tuple(sorted(j)))
        return [list(i) for i in res]

                    

if __name__ == "__main__":
    s = Solution()
    print(s.combinationSum([2,3,6,7],7))#[7],[2,2,3]
    print(s.combinationSum([2,3,5], 8))# [2,2,2,2],[2,3,3],[3,5]
    print(s.combinationSum([2],1))