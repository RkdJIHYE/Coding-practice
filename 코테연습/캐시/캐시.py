def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        answer = len(cities)*5
        return answer
    
    #대소문자 구분 안한다고 했으니까 전체를 소문자 변경 필요
    newcities =[]
    for k in cities:
        newcities.append(k.lower())

    cc = ['']*cacheSize
    tmp=0
    for i in newcities:
        if i not in cc:
            tmp=tmp%cacheSize
            cc[tmp]=i
            tmp+=1
            answer+=5
        else:
            answer+=1
     
    return answer


