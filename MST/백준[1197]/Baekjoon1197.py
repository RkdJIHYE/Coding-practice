import sys
import heapq
input = sys.stdin.readline

V, E = map(int,input().split())

edge = [ [] for _ in range(V+1)]
chk  = [False]*(V+1)

for i in range(E):
    a,b,c= map(int,input().split())
    #양방향 리스트이기에 둘다 넣어주기
    edge[a].append([c,b])
    edge[b].append([c,a])
    
rs = 0   

heap = [[0,1]] 
#시작점 1번 vertex

while heap:
    w, each_node = heapq.heappop(heap)
    #방문 안했는지 먼저 체크 
    if chk[each_node] == False:
        chk[each_node]=True
        rs +=w
        for next_edge in edge[each_node]:
            if chk[next_edge[1]]==False:
                heapq.heappush(heap,next_edge)
    
    
print(rs)