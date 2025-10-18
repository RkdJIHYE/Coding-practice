def solution(n, w, num):
    # n는 택배 상자 개수
    # w 가로 길이
    # num 꺼내고싶은 상자 번호
    answer = 0
    #좌 우 이동을 위한 변수
    pt = 0
    cnt = n//w +1
    li = [[0]*w for _ in range(cnt)]
    print(li)
    #시작 위치
    x=0
    y=0
    chk = True
    tmp = 1 #1부터 시작
    for i in range(len(li)-1,-1,-1):
        if chk == True:  
            for j in range(len(li[i])):
                chk = False
                li[i][pt]=tmp
                tmp+=1
                pt+=1
                if tmp >n:
                    break
        elif chk == False:
            for j in range(len(li[i])):
                chk = True
                li[i][pt]=tmp
                tmp+=1
                pt-=1
                if tmp >n:
                    break
    print(li)
    return answer