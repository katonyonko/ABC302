import io
import sys

_INPUT = """\
6
6 6
vgxgpu
amkxks
zhkbpp
hykink
esnuke
zplvfj
5 5
ezzzz
zkzzz
ezuzs
zzznz
zzzzs
10 10
kseeusenuk
usesenesnn
kskekeeses
nesnusnkkn
snenuuenke
kukknkeuss
neunnennue
sknuessuku
nksneekknk
neeeuknenk
"""

def solve(test):
  H,W=map(int,input().split())
  S=[input() for _ in range(H)]
  d=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
  for i in range(H):
    for j in range(W):
      for k in range(8):
        x=[]
        for l in range(5):
          if 0<=i+l*d[k][0]<H and 0<=j+l*d[k][1]<W:
            x.append(S[i+l*d[k][0]][j+l*d[k][1]])
        if ''.join(x)=='snuke':
          ans=[(i+l*d[k][0]+1,j+l*d[k][1]+1) for l in range(5)]
  if test==0:
    for i in range(5):
      print(*ans[i])
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