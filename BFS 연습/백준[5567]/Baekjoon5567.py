import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())

map = [list(map(int,input().split())) for _ in range(m)]

chk = [False]*(n+1)

def bfs(y,x):
    q=[(y,x)]
    while q:
        d
        
    return 0 
        
fr = []

while fr:     
    for j in range (m):
        if map[j][0]==1 and chk[(map[j][1])]==False:
            chk[(map[j][1])]==True
            fr.append(map[j][1])
        
        
    
    
print(sum(chk))