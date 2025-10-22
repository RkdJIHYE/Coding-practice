def solution(msg):
    answer = []
    li = ['0','A','B','C','D','E','F','G','H','I','J','K',
          'L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    
    i = 0
    while i < len(msg):
        # 현재 위치에서 가장 긴 문자열 w 찾기
        w = msg[i]
        while i + len(w) < len(msg) and msg[i:i+len(w)+1] in li:
            w = msg[i:i+len(w)+1]
        
        # 현재 w의 인덱스 추가
        answer.append(li.index(w))
        
        # 사전에 새로운 단어 추가 (w + 다음 문자)
        if i + len(w) < len(msg):
            li.append(w + msg[i + len(w)])
        
        # 다음 위치로 이동
        i += len(w)
    
    return answer
