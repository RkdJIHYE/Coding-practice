import sys

input = sys.stdin.readline

n = int(input())

#주어진 입력이 띄어 있지 않은 경우 split() 대신 strip() 사용
danzi = [list(map(int,input().strip())) for _ in range(n)]
#해당 위치에 방문했는지 여부 나타내기 
chk = [[False]*n for _ in range(n)]


#전체 몇 묶음인지를 확인하는 변수
cnt = 0

def bfs(q):
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    #이동을 위한 값
    #전체 이동(한 묵음)
    tot=1
    while q :
        x,y = q.pop()
        #방향 4개 확인하기 
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            #새로 만든 좌료가 범위 안에 있는지 확인
            if 0<=nx<n and 0<=ny<n and chk[nx][ny]==False and danzi[nx][ny]==1:
                chk[nx][ny]=True
                tot+=1
                q.append([nx,ny])
            else:
                continue
            
    return tot


res =[]

for i in range(n):
    for j in range(n):
        if danzi[i][j]==1 and chk[i][j]==False:
            chk[i][j]=True
            cq=[[i,j]]
            re=bfs(cq)
            cnt += 1
            res.append(re)
        else:
            continue
        
#실행 결과값

res.sort()
print(f'총 집단수는 {cnt}개 입니다.')
for k in range(len(res)):
    print(res[k])
