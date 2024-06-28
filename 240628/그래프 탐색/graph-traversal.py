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
    global ncnt
    for idx,val in enumerate(arr[node]):
        #print(f"idx,val:{idx},{val}")
        if val == CONNECTED:
            if visit[node] == VISITED:
                return
            else:
                visit[node] = VISITED
                ncnt += 1
                count_nodes(idx)
    return

connect_nodes()
count_nodes(1)
print(ncnt)