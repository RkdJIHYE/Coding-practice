import sys
input = sys.stdin.readline

n,m = map(int,input().split())

Map = list(map(int,input().split()))

#m개의 연속된 수 중에 가장 큰 값 반환하는 것 ?

#위치 초기화
st = 0
rs =0
for i in range(m):
    rs+=Map[i]
max_val = rs

for j in range(m,n):
    new_val = rs - Map[st]+Map[j]
    st+=1
    if new_val>max_val:
        max_val=new_val
    rs = new_val
print(max_val)
    

