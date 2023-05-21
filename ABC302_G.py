import io
import sys
from itertools import accumulate

_INPUT = """\
6
6
3 4 1 1 2 4
4
2 3 4 1
"""

def solve(test):
  N=int(input())
  A=list(map(lambda x:int(x)-1,input().split()))
  cnt=[A.count(i) for i in range(4)]
  acnt=list(accumulate(cnt))
  g=[[0]*4 for _ in range(4)]
  for i in range(N):
    for j in range(4):
      if i<acnt[j]:
        g[A[i]][j]+=1
        break
  ans=0
  for i in range(4):
    for j in range(4):
      if i!=j:
        tmp=min(g[i][j],g[j][i])
        ans+=tmp
        g[i][j]-=tmp
        g[j][i]-=tmp
  for i,j,k in [(1,2,3),(1,0,2),(2,1,3),(0,1,2),(0,2,3),(2,0,3),(0,1,3),(1,0,3)]:
    tmp=min(g[i][j],g[j][k],g[k][i])
    ans+=2*tmp
    g[i][j]-=tmp
    g[j][k]-=tmp
    g[k][i]-=tmp
  tmp=min(g[0][1],g[1][2],g[2][3],g[3][0])
  ans+=3*tmp
  g[0][1]-=tmp
  g[1][2]-=tmp
  g[2][3]-=tmp
  g[3][0]-=tmp
  tmp=min(g[0][3],g[1][0],g[2][1],g[3][2])
  ans+=3*tmp
  g[0][3]-=tmp
  g[1][0]-=tmp
  g[2][1]-=tmp
  g[3][2]-=tmp
  tmp=min(g[0][3],g[1][2],g[2][0],g[3][1])
  ans+=3*tmp
  g[0][3]-=tmp
  g[1][2]-=tmp
  g[2][0]-=tmp
  g[3][1]-=tmp
  tmp=min(g[0][2],g[1][3],g[2][1],g[3][0])
  ans+=3*tmp
  g[0][2]-=tmp
  g[1][3]-=tmp
  g[2][1]-=tmp
  g[3][0]-=tmp
  tmp=min(g[0][2],g[1][0],g[2][3],g[3][1])
  ans+=3*tmp
  g[0][2]-=tmp
  g[1][0]-=tmp
  g[2][3]-=tmp
  g[3][1]-=tmp
  tmp=min(g[0][1],g[1][3],g[2][0],g[3][2])
  ans+=3*tmp
  g[0][1]-=tmp
  g[1][3]-=tmp
  g[2][0]-=tmp
  g[3][2]-=tmp
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