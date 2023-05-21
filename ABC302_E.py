import io
import sys

_INPUT = """\
6
3 7
1 1 2
1 1 3
1 2 3
2 1
1 1 2
2 2
1 1 2
2 1
2 1
"""

def solve(test):
  N,Q=map(int,input().split())
  G=[set() for _ in range(N)]
  ans=N
  for _ in range(Q):
    query=input()
    if query[0]=='1':
      d,u,v=map(lambda x: int(x)-1,query.split())
      G[u].add(v)
      G[v].add(u)
      if len(G[u])==1: ans-=1
      if len(G[v])==1: ans-=1
      print(ans)
    else:
      d,u=map(lambda x: int(x)-1,query.split())
      if len(G[u])==0: print(ans)
      else:
        ans+=1
        tmp=G[u].copy()
        for v in tmp:
          G[u].remove(v)
          G[v].remove(u)
          if len(G[v])==0: ans+=1
        print(ans)

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