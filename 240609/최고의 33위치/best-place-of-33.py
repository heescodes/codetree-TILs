#2:24
N = int(input())
arr = []
coins = 0
for _ in range(N):
    arr.append([int(nums) for nums in input().split()])

def scan_3x3(y,x):
    res = 0
    for a in range(y,y+3):
        for b in range(x, x+3):
            #print("arr[%d][%d]: %d" % (a,b,arr[a][b]))
            if arr[a][b] == 1:
                res += 1
    return res

for i in range(N-2):
    for j in range(N-2):
        cmp_coin = scan_3x3(i,j)
        #print(f'cmp_coin:{cmp_coin}')
        coins = max(coins, cmp_coin)
print(coins)