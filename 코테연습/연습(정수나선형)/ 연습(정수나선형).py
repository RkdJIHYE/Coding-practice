def solution(n):
    if n <= 0:
        return []

    answer = [[0] * n for _ in range(n)]
    visited = [[False] * n for _ in range(n)]

    # 오른쪽, 아래, 왼쪽, 위 (시계 방향)
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    y, x = 0, 0
    dir_idx = 0
    k = 1
    max_k = n * n

    while k <= max_k:
        answer[y][x] = k
        visited[y][x] = True
        k += 1

        ny = y + dy[dir_idx]
        nx = x + dx[dir_idx]

        # 다음 칸이 유효하고 미방문이면 이동, 아니면 방향 바꾸기
        if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
            y, x = ny, nx
        else:
            dir_idx = (dir_idx + 1) % 4
            y += dy[dir_idx]
            x += dx[dir_idx]

    return answer
