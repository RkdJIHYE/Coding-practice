def solution(dartResult):
    answer = 0

    #li에는 계산한 결과값 저장 
    li = []
    #1부터 10까지 숫자 
    i=0
    while i<len(dartResult):
        if dartResult[i].isdigit() and dartResult[i+1]!='0':
            li.append(int(dartResult[i]))
            i+=1
        elif dartResult[i].isdigit() and dartResult[i+1]=='0':
            li.append(10)
            i+=2
        elif dartResult[i]=='S':
            i+=1
        elif dartResult[i]=='D':
            tmp=li.pop()
            li.append(tmp**2)
            i+=1
        elif dartResult[i]=='T':
            tmp=li.pop()
            li.append(tmp**3)
            i+=1
        elif dartResult[i]=='*':
            if len(li)<=1:
                tmp = li.pop()
                li.append(tmp*2)
            else:
                tmp1 = li.pop()
                tmp2 = li.pop()
                li.append(tmp2*2)
                li.append(tmp1*2)
            i+=1
        elif dartResult[i]=='#':
            tmp = li.pop()
            li.append(tmp*(-1))
            i+=1     
                       
    for j in li:
        answer+=j
    return answer