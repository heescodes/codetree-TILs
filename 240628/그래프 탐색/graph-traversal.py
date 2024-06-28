CONNECTED=1
VISITED=1
N_VISITED=0
ncnt = 0

N,M = map(int,input().split())

arr = list(list(0 for _ in range(N+1)) for _ in range(N+1))
visit = [0]*(N+1)

def connect_nodes():
    for _ in range(M):
        a,b = map(int, input().split())
        arr[a][b] = 1
        arr[b][a] = 1

def count_nodes(node):
    if M == 0:
        return
    global ncnt
    for v in range(1, N+1):
        if arr[node][v] == CONNECTED and visit[v] == N_VISITED:
            visit[v] = VISITED
            ncnt += 1
            count_nodes(v)
    return

connect_nodes()
count_nodes(1)
print(ncnt)