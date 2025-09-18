import sys

input = sys.stdin.readline
INF = sys.maxsize

V = int(input())
N = int(input())

chk = [[] for _ in range(V+1)]
rs = [[INF]*(V+1) for _ in range(V+1)]

for i in range(1,V+1):
    rs[i][i]=0
    
for i in range(N):
    u,v,w = map(int,input().split())
    
    rs[u][v]=min(rs[u][v],w)

for k in range(1,V+1): #중간
    for j in range(1,V+1): #시작
        for i in range(1,V+1): #도착
            if rs[j][i]>rs[j][k]+rs[k][i]:
                rs[j][i]=rs[j][k]+rs[k][i]
                
print()
for j in range(1,V+1):
    for i in range(1,V+1):
        if rs[j][i]==INF : print(0,end=' ')
        else : print(rs[j][i],end=' ')
    print()



