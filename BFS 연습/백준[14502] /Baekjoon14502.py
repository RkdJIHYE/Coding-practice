import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

empties = []   # 0인 칸들
viruses = []   # 2인 칸들
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empties.append((i, j))
        elif graph[i][j] == 2:
            viruses.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def spread_and_count(grid):
    """grid는 벽이 이미 세워진 상태의 복사본.
    바이러스를 BFS로 퍼뜨리고 남은 0(안전영역) 개수를 반환."""
    q = deque(viruses)
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and grid[nx][ny] == 0:
                grid[nx][ny] = 2
                q.append((nx, ny))
    # 안전영역 개수 반환
    return sum(row.count(0) for row in grid)

max_safe = 0
# 빈칸 3개 조합으로 벽 세우기
for a, b, c in combinations(empties, 3):
    # 원본 건드리지 않도록 복사
    grid_copy = [row[:] for row in graph]
    grid_copy[a[0]][a[1]] = 1
    grid_copy[b[0]][b[1]] = 1
    grid_copy[c[0]][c[1]] = 1

    safe = spread_and_count(grid_copy)
    if safe > max_safe:
        max_safe = safe

print(max_safe)
