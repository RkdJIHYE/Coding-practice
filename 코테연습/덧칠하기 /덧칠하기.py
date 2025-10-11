def solution(n, m, section):
    answer = 0
    chk = [True]*(n+1)
    for i in section:
        chk[i]=False

    
    for j in range(len(chk)):
        if chk[j]==True:
            continue
        else:
            answer+=1
            for k in range(m):
                if j+k<len(chk):
                    chk[j+k]=True
                else:
                    break

        
    return answer