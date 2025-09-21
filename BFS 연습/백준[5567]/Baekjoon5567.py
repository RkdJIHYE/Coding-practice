import sys
import heapq
input = sys.stdin.readline

n = int(input())
m = int(input())

f= [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    f[a].append(b)
    f[b].append(a)

chk = [False]*(n+1)
fone = f[1]

if not fone:
    print(0)

else:
    for i in fone:
        if chk[i]==False:
            chk[i]=True
            for next_edge in f[i]:
                if chk[next_edge]==False:
                    chk[next_edge]=True
    print(sum(chk))
