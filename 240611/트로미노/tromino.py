X=0
Y=1
n, m = map(int, input().split())
arr = [list(map(int,input().split())) for _ in range(n)]

def type1_max_search():
    res = 0
    for a in range(m):
        for b in range(n):
            tmp1,tmp2,tmp3,tmp4 = 0,0,0,0 
            cen = (a,b)
            #case └
            if (cen[Y]-1 >= 0) and (cen[X]+1 <= m-1):
                tmp1 = arr[b][a] + arr[b-1][a] + arr[b][a+1]
            #case ┘
            if (cen[Y]-1 >= 0) and (cen[X]-1 >= 0):
                tmp2 = arr[b][a] + arr[b-1][a] + arr[b][a-1]
            #case ┌
            if (cen[Y]+1 <= n-1) and (cen[X]+1 <= m-1):   
                tmp3 = arr[b][a] + arr[b+1][a] + arr[b][a+1]    
            #case ┐
            if (cen[Y]+1 <= n-1) and (cen[X]-1 >= 0):   
                tmp4 = arr[b][a] + arr[b+1][a] + arr[b][a-1]
            res = max(res,tmp1,tmp2,tmp3,tmp4)
    return res


def type2_max_search():
    res = 0
    for a in range(m):
        for b in range(n):
            tmp1,tmp2 = 0,0 
            cen = (a,b)
            #case ㅣ
            if (cen[Y]-1 >= 0) and (cen[Y]+1 <= n-1):
                tmp1 = arr[b][a] + arr[b-1][a] + arr[b+1][a]
            #case ㅡ
            if (cen[X]-1 >= 0) and (cen[X]+1 <= m-1):
                tmp2 = arr[b][a] + arr[b][a-1] + arr[b][a+1]
            res = max(res,tmp1,tmp2)
    return res

#print(type1_max_search(), type2_max_search())
print(max(type1_max_search(), type2_max_search()))