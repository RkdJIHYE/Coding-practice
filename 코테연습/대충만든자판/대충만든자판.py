import math

def solution(keymap, targetas):
    answer = []
    for i in targets: # 타겟에 있는 내용 하나 추출 
        rs = 0
        for j in i: # 글자 하나하나 비교하기 위함
            tmp = math.inf
            for k in keymap: # 키맵에 있는 내용 비교 
                if j in k:
                    tmp = min(tmp,k.index(j)+1)
                else:
                    continue
            rs+=tmp
        if rs!=math.inf:
            answer.append(rs)
        else:
            answer.append(-1)
    return answer