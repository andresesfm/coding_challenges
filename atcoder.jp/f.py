#  https://atcoder.jp/contests/dp/tasks/dp_f

ss='axyb'
tt='abyxb'
expected ='axb'

def max_sub_string():
  # DP[i][j] = number of matching characters up to position i,j
  DP=[[0]*(len(ss)+1) for i in range(len(tt)+1)]
  #longest string up to here
  DPs=[[(0,0)]*(len(ss)+1) for i in range(len(tt)+1)]
  for i in range(len(tt)):
    for j in range(len(ss)):
      if tt[i]==ss[j]:
        if DP[i+1][j+1]< DP[i][j]+1:
          DP[i+1][j+1] =  DP[i][j]+1
          DPs[i+1][j+1]=(i,j) 
      
      if DP[i+1][j]<DP[i][j]:
        DP[i+1][j] = DP[i][j]
        DPs[i+1][j]=(i,j)
      if DP[i][j+1]<DP[i][j]:
        DP[i][j+1] = DP[i][j]
        DPs[i][j+1]=(i,j)

  print(DP)
  print(DPs)
  result = 0
  ress = (0,0)
  for i in range(len(tt)):
    for j in range(len(ss)):
      if result <DP[i][j]:
        result = DP[i][j]
        ress = (i,j)
  return result

print(max_sub_string())