#12:12
n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append([int(nums) for nums in input().split()])

res = 0

def is_in_range(x,y,w,l):
    if (0 <= x <= m-w) and (0 <= y <= n-l):
        return True
    else:
        return False

def is_valid_squ(x,y,w,l):
    for i in range(x,x+w):
        for j in range(y,y+l):
            if arr[j][i] <= 0:
                return False
    return True

for r in range(n):
    for c in range(m):
        for w in range(1,m-r+1):
            for l in range(1,n-c+1):
                if is_valid_squ(r,c,w,l) == True:
                    res = max(res, w*l)

if res == 0:
    print(-1)
else:
    print(res)