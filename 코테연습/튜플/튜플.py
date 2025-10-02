def solution(s):
    answer = []
    s=s.split(',')
    
    print(s)
    for j in s:
        print(j)
        print()
    
    
    for str in s:
        tmp = ''
        for j in str:
            if j.isdigit():
                tmp +=j
                
        if int(tmp) not in answer: 
            answer.append(int(tmp))
        
    
    return answer