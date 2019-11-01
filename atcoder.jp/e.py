#Knapsack 1
# https://atcoder.jp/contests/dp/tasks/dp_e

#number of items
N = 3
#max weight
W = 8
ws=[3,4,5]
vs=[30,50,60]

INF = 1e9+5

def max_values():
  #DP[i] =min total weight of items with total value exactly i
  sum_values = sum(vs)
  DP =[INF]*(sum_values+1)
  DP[0]=0
  for i in range(N):
    value = vs[i]
    weight= ws[i]
    for currentValue in range(sum_values-value,-1,-1):
      DP[currentValue+value] = min(DP[currentValue+value],DP[currentValue]+weight)

  result = 0
  for i in range(sum_values+1):
    if DP[i]<=W:
      result = max(result,i)
  print(DP)
  return result


print(max_values())