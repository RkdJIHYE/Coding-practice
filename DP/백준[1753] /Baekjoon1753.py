import sys

input = sys.stdin.readline

N =int(input())

fib = [0,1]

def fibo(N):
    
    if N>1:
        for i in range(2,N+1):
            rs = fib[i-2]+fib[i-1]
            fib.append(rs)
            
    return fib[N]
    
if N==0:
    print(N)
    print(N)
    
elif N<0:
    print(-1)
    N=abs(N)
    print(fibo(N))
    
else:
    print(1)
    print(fibo(N))
    
    
    