import sys

input = sys.stdin.readline

n = int (input())

#    0개1개2개 (방안)
rs = [0,1,2]

for i in range(3,n+1):
    rs.append((rs[i-2]+rs[i-1])%10007)
    
    
print(rs[n])