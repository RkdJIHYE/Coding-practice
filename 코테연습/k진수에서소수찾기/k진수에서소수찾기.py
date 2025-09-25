def solution(id_list, report, k):
    answer = []
    user = [0]*len(id_list)
    li = [[] for _ in range(len(id_list))]
    rs = len(id_list)*[0]
    report = set(report)

    
    for i in report:
        st,ed = i.split()
        tmp=id_list.index(st)
        tmp2=id_list.index(ed)
        li[tmp].append(ed)
        user[tmp2]+=1
        
    stop = []
    for h in range(len(user)):
        if user[h]>=k:
            stop.append(id_list[h])

    for j in li:
        cnt=0
        for i in j:
            if i in stop:
                cnt +=1
        answer.append(cnt)
    
    return answer