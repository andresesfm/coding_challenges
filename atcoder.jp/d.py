#Knapsack 1
# https://atcoder.jp/contests/dp/tasks/dp_d

#number of items
N = 3
#max weight
W = 8
ws=[3,4,5]
vs=[30,50,60]

def max_values():
  #DP[i] =max total value of items with total weight exactly i
  DP =[0]*(W+1) 
  for i in range(N):
    weight = ws[i]
    value = vs[i]
    for currentWeight in range(W-weight,-1,-1):
      DP[currentWeight+weight] = max(DP[currentWeight+weight],DP[currentWeight]+value)

  result = 0
  for i in range(W+1):
    result = max(result,DP[i])
  print(DP)
  return result


print(max_values())