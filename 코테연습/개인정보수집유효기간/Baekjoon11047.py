def solution(today, terms, privacies):
    answer = []
    termHash ={}
    for s in terms:
        month = s[2:]
        termHash[s[0]] = int(month)*28
    
    td = int(today[2:4])*12*28 + int(today[5:7])*28 + int(today[8:])
    
    i = 1
    for s in privacies:
        tmp=int(s[2:4])*12*28 + int(s[5:7])*28 + int(s[8:10])
        if td - tmp >= termHash[s[11]]:
            answer.append(i)
            
        i+=1

    return answer