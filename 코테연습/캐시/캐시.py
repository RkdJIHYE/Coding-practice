#캐시 교체 알고리즘 -> LRU 가장 오래된 것 먼저 제거하기

def solution(cacheSize, cities):
    answer = 0
    if cacheSize==0:
        answer = len(cities)*5
        return answer

    cc = []
    for i in cities:
        cn = i.lower()
        
        if cn in cc:
            cc.remove(cn)
            cc.append(cn)
            answer+=1
        else:
            if len(cc)<cacheSize:
                cc.append(cn)
            else:
                cc.pop(0)
                cc.append(cn)
            answer+=5
                
     
    return answer


