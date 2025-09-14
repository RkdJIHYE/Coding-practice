import sys
input = sys.stdin.readline

n = int(input())
map = [list(map(int,input().strip())) for _ in range (n)]
#strip -> 붙어 있는 문자열이라 저렇게 사용하였다.

chk = [[False]*n for _ in range(n)]
rs =[]
each =0
dy=[0,1,0,-1]
dx=[1,0,-1,0]

def dfs(y,x):
    global each #전역함수로 바꿔주는 것 필요하다. 
    each+=1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        
        if 0<=ny<n and 0<=nx<n:
            if map[ny][nx]==1 and chk[ny][nx]==False:
                chk[ny][nx]=True
                dfs(ny,nx)    
        

for j in range (n):
    for i in range(n):
        if map[j][i]==1 and chk[j][i]==False:
            chk[j][i]=True
            each=0
            dfs(j,i)
            rs.append(each)
            
            
rs.sort()
print(len(rs))
for i in rs:
    print(i)