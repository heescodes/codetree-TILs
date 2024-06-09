#2:24
N = int(input())
arr = []
coins = 0
for _ in range(N):
    arr.append([int(nums) for nums in input().split()])
#arr = [list(map(int, input.split())) for _ in range(n)]

def scan_3x3(y,x):
    res = 0
    for a in range(y,y+3):
        for b in range(x, x+3):
            if arr[a][b] == 1:
                res += 1
    return res

for i in range(N-2):
    for j in range(N-2):
        cmp_coin = scan_3x3(i,j)
        coins = max(coins, cmp_coin)
print(coins)