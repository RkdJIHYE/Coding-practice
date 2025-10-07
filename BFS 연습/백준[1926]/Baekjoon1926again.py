import sys

input = sys.stdin.readline

n,m = map(int,input().split())
map = [list(map(int,input().split())) for _ in range (n)]
chk = [[False]* m for _ in range(n)]

dy = [0,0,1,-1]
dx = [1,-1,0,0]

def bfs(y,x):
    rs=1
    q = [(y,x)]
    while q:
        ey,ex = q.pop()
        for k in range(4):
            ny = ey + dy
            nx = ex + dx
            
            if 0<=ny<n and 0<=nx <n:
                if map[ny][nx] == 1 and chk [ny][nx]==False:
                     chk[ny][nx]=True
                     rs+=1
                     q.append((ny,nx))
                     
    return rs


cnt = 0
maxv = 0

for j in range(n):
    for i in range(m):
        # 방문하지 않았으면서 갈 수 있는 경우 
        if map[j][i] == 1 and chk[j][i]== False:
            #전체 그림 개수 +1
            #BFS > 그림 크기를 구하고
            #최댓값 갱신
            
            chk [j][i]=True
            cnt +=1
            maxv = max(maxv,bfs(j,i))
            
print(cnt)
print(maxv)