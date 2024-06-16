#12:12
n, m = map(int,input().split())
arr = []
for i in range(n):
    arr.append([int(nums) for nums in input().split()])

res = 0

def is_in_range(x,y,w,l):
    if (0 <= x <= m-w) and (0 <= y <= n-l):
        #print("range true")
        return True
    else:
        #print("range false")
        return False

def is_valid_squ(x,y,w,l):
    for j in range(y,y+l):
        for i in range(x,x+w):
            if arr[j][i] <= 0:
                #print("square false")
                return False
    #print("square true")
    return True

for r in range(n): #y
    for c in range(m): #x
        for l in range(1,n-r+1): #y
            for w in range(1,m-c+1): #x
                #print(f'r,c,w,l : {r},{c},{w},{l}')
                #print("----------------")
                if is_in_range(c,r,w,l) and is_valid_squ(c,r,w,l):
                    res = max(res, w*l)

if res == 0:
    print(-1)
else:
    print(res)