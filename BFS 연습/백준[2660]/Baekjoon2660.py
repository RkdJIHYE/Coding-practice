import sys

input = sys.stdin.readline

n = int(input().strip())

cnt = [0]*(n+1)


x,y = map(int,(input().split()))
while x!=-1:
    cnt[x]+=1
    cnt[y]+=1
    
    x,y = map(int,(input().split()))

print(cnt)