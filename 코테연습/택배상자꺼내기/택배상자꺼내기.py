def solution(n, w, num):
    # n는 택배 상자 개수
    # w 가로 길이
    # num 꺼내고싶은 상자 번호
    answer = 0
    
    cnt = n//w +1
    li = [[0]*w for _ in range(cnt)]
    print(li)
    #시작 위치
    x=0
    y=0
    chk = True
    tmp = 1 #1부터 시작
    #좌 우 이동을 위한 변수
    
    for i in range(len(li)-1,-1,-1):
        if chk == True:
            pt = 0
            chk = False
            for j in range(len(li[i])):
                if tmp == num :
                    y=i
                    x=pt
                li[i][pt]=tmp
                tmp+=1
                pt+=1
                if tmp >n:
                    break
        elif chk == False:
            pt = w-1
            chk = True
            for j in range(len(li[i])):
                if tmp == num :
                    y=i
                    x=pt
                li[i][pt]=tmp
                tmp+=1
                pt-=1
                if tmp >n:
                    break
                    
    if li[0][x]!=0:
        answer=y+1
    else:
        answer=y
    return answer