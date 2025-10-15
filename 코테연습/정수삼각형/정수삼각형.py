def solution(triangle):
    answer = 0
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            triangle[i][j]+=triangle[i-1][j-1]
                       
                       
    print(triangle)
    return answer