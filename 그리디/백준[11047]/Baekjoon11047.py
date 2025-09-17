import sys

input = sys.stdin.readline

N,money = map(int,input().split())

li = []

for i in range(N):
    li.append(int(input()))

li.sort(reverse=True)

chk = [0]*N

i=0

while money>0:
    for check in li :
        cnt = money // check 
        chk[i]=cnt
        i+=1
        money = money - cnt*check
        
answer = sum(chk)

print(answer)