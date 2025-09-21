
import sys

input = sys.stdin.readline


# 기준이 되는 것 
N = int(input())
list_A = list(map(int,input().split()))
list_A.sort()
# 분석해야하는 것 
M = int(input())
list_B = list(map(int,input().split()))

#이진 탐색 코드 작성
def search (st,ed,target):
    if st == ed :
        if list_A[st]==target:
            print(1)
        else: 
            print(0)
        return
            
    mid = (st+ed)//2
    
    if list_A[mid]<target:
        search(mid+1,ed,target)
    else:
        search(st,mid,target)
      
      
for target_number in list_B:
    search(0,N-1,target_number)  
    
