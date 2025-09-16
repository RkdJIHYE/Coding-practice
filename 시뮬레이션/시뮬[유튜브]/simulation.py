import sys

input = sys.stdin.readline

board =list(map(int, input().split(',')))
n = len(board)
cnt=0
while 1:
    chk = False # 밑의 for 문을 돌았는지 안 돌았는지 확인 할 수 있는 chk 
    nmap=[0]*n
    for i in range(n):
        if (board[i]<2): continue
        chk = True
        #왼쪽 끝
        if i==0:
            board[i]-=2
            nmap[i+1]+=1
        #오른쪽 끝    
        elif i==n-1:
            board[i]-=2
            nmap[i-1]+=1
        #사이에 있는 경우  
        else:
            board[i]-=2
            nmap[i+1]+=1
            nmap[i-1]+=1
        
    if chk == False:
        break
    for i in range(n):
        board[i]+=nmap[i]
    cnt+=1
    
print(board)
print(cnt)
        
    


