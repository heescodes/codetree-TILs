from collections import deque

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def is_snake(x, y):
    return arr[x][y] == 0

def get_minlen():
    q = deque([(0, 0)])
    visited = [[False] * m for _ in range(n)]
    distance = [[0] * m for _ in range(n)]
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        if x == n-1 and y == m-1:
            return distance[x][y]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if in_range(nx, ny) and not is_snake(nx, ny) and not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = True
                distance[nx][ny] = distance[x][y] + 1

    return -1

result = get_minlen()
print(result)