import sys
import heapq
input = sys.stdin.readline

# V는 vertex E 는 edge
V,E = map(int,input().split())

st = int(input())
INF = sys.maxsize

dist =[INF]*(V+1)
            #시작점
# 1번 과 연결된것 [1][[가중치],[도착점]]
# 이렇게 표시하기 위함
edge = [ [] for _ in range(V+1)]

for i in range(E):
    u,v,w = map(int,input().split())
    edge[u].append([w,v])
       
dist[st]=0
heap = [[0,st]]

while heap:
    # 현재 있는 값 
    ew, ev = heapq.heappop(heap)
    if dist[ev] != ew : continue
    for nw, nv in edge[ev]:
        if dist[nv] > ew + nw :
            dist[nv] = ew+nw
            heapq.heappush(heap,[dist[nv],nv])

for i in range(1,V+1):
    if dist[i]==INF: print("INF")
    else: print(dist[i])
    
        