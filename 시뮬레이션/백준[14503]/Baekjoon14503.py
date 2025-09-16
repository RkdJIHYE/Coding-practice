import sys
input = sys.stdin.readline

N, M = map(int, input().split())
y, x, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
dy = [-1, 0, 1, 0]  # 북, 동, 남, 서
dx = [0, 1, 0, -1]

while True:
    # 1) 현재 칸 청소
    if map[y][x] == 0:
        map[y][x] = 2
        cnt += 1

    #움직였는지 확인하는 코드 
    moved = False
    # 2) 왼쪽부터 4방향 탐색
    for i in range(1, 5):
        nd = (d - i) % 4
        ny = y + dy[nd]
        nx = x + dx[nd]
        if 0 <= ny < N and 0 <= nx < M and map[ny][nx] == 0:
            d = nd
            #y,x 좌표 갱신해주기 
            y, x = ny, nx
            moved = True
            break

    # 3) 네 방향 모두 불가 → 뒤로 후진 or 종료
    if not moved:
        back = (d+2)%4
        #뒤로 갔을때의 좌표 
        by = y + dy[back]
        bx = x + dx[back]
        if not (0 <= by < N and 0 <= bx < M):  # 범위 밖이면 종료
            break
        if map[by][bx] == 1:  # 벽이면 종료
            break
        y, x = by, bx  # 후진(방향은 유지)

print(cnt)
