import sys

input = sys.stdin.readline

#m:열  n:행 
m,n = map(int,(input().split()))

tomato =[list(map(int,input().split())) for _ in range(n)]

chk = [[False]*m for _ in range(n)]
print(tomato)

#최소 day를 체크하는 변수 tot
tot = 0

def bfs(x,y):
    #위 아래 좌 우 위치 
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        #새로 만든 nx ny가 배열의 범위를 벗어나진 않는지 체크
        
        if 0<=nx<m and 0<=ny<n and chk[nx][ny]==False:
            chk[nx][ny]=True
            tomato[nx][ny]=1
        else:
            continue
        
    
    
print(chk)