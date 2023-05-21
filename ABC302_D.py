import io
import sys
from bisect import bisect_left,bisect_right

_INPUT = """\
6
2 3 2
3 10
2 5 15
3 3 0
1 3 3
6 2 7
1 1 1000000000000000000
1000000000000000000
1000000000000000000
8 6 1
2 5 6 5 2 1 7 9
7 2 5 5 2 4
"""

def solve(test):
  N,M,D=map(int,input().split())
  A=list(map(int,input().split()))
  B=list(map(int,input().split()))
  ans=-1
  A.sort()
  B.sort()
  for i in range(N):
    idx=bisect_right(B,A[i]+D)-1
    if idx>=0 and B[idx]>=A[i]-D:
      ans=max(ans,A[i]+B[idx])
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