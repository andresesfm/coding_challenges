#https://atcoder.jp/contests/dp/tasks/dp_g
import sys

nax = 10e5+5

line_count = 0
for line in sys.stdin:
  if line_count==0:
    N,M = [int(i) for i in line.split(" ")]
    print(N,M)
    E= [[]*M for i in range(N+1)]
    in_degree = [0]*(M)# number 0f edges directed to vertix i
  else:
    a,b = [int(i) for i in line.split(" ")]
    print(a,b)
    E[a].append(b)
    in_degree[b]+=1
  line_count+=1

# E[1].append(2) 
# E[1].append(3)
# E[3].append(2)
# E[2].append(4)
# E[3].append(4)


dist = [0]*(N) #distance up to vertix i
visited = [False]*(N) # has item been visited

def DFS(a):
  assert not visited[a]
  visited[a] = True
  for b in E[a]:
    dist[b] = max(dist[b],dist[a]+1)
    in_degree[b]-=1
    if in_degree[b] != 0:
      DFS(b)

for i in range(N):
  if not visited[i] and in_degree[i]==0:
    DFS(i)

result = 0
for d in range(N):
  result=max(result,dist[d])
print(E)
print(dist)
print(visited)
print(result)