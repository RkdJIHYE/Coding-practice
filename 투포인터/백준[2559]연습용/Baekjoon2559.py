#투포인터 - 수열 2559

import sys
input = sys.stdin.readline

#n은 총 개수 , m은 더하는 크기 
n,m = map(int,input().split())

chk = list(map(int,input().split()))

#온도합이 제일 큰 것 찾기 

max_n =0
cur_n = 0
for j in range(m):
    cur_n+=chk[j]

max_n=cur_n
st = 0
ed = m-1
#시행 횟수 n-m+1과 같다 
for i in range(n-m):
    cur_n-=chk[st]
    cur_n+=chk[ed+1]
    
    if cur_n>max_n:
        max_n=cur_n
        
    st+=1
    ed+=1

print(chk)
print(max_n)