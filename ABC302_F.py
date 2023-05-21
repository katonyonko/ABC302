import io
import sys
from collections import defaultdict
from collections import deque

_INPUT = """\
6
3 5
2
1 2
2
2 3
3
3 4 5
1 2
2
1 2
3 5
2
1 3
2
2 4
3
2 4 5
4 8
3
1 3 5
2
1 2
3
2 4 7
4
4 6 7 8
"""

def solve(test):
  N,M=map(int,input().split())
  dist=[10**20]*N
  di=defaultdict(list)
  used=[0]*M
  G=[]
  dq=deque()
  for i in range(N):
    A=int(input())
    G.append(set(list(map(lambda x:int(x)-1,input().split()))))
    for j in G[-1]:
      di[j].append(i)
    if 0 in G[-1]:
      dist[i]=0
      dq.append(i)
      used[0]=1
  while dq:
    x=dq.popleft()
    for y in G[x]:
      if used[y]==1: continue
      used[y]=1
      for v in di[y]:
        if dist[v]>dist[x]+1:
          dist[v]=dist[x]+1
          dq.append(v)
  ans=10**20
  for i in range(N):
    if M-1 in G[i]:
      ans=min(ans,dist[i])
  if ans==10**20: ans=-1
  if test==0:
    print(ans)
  else:
    return None

def random_input():
  from random import randint,shuffle
  N=randint(1,10)
  M=randint(1,N)
  A=list(range(1,M+1))+[randint(1,M) for _ in range(N-M)]
  shuffle(A)
  return (" ".join(map(str, [N,M]))+"\n"+" ".join(map(str, A))+"\n")*3

def simple_solve():
  return []

def main(test):
  if test==0:
    solve(0)
  elif test==1:
    sys.stdin = io.StringIO(_INPUT)
    case_no=int(input())
    for _ in range(case_no):
      solve(0)
  else:
    for i in range(1000):
      sys.stdin = io.StringIO(random_input())
      x=solve(1)
      y=simple_solve()
      if x!=y:
        print(i,x,y)
        print(*[line for line in sys.stdin],sep='')
        break

#0:提出用、1:与えられたテスト用、2:ストレステスト用
main(0)