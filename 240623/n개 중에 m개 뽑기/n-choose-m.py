n,m = map(int, input().split())
result = []

def print_res():
    print(" ".join(map(str, result)))
    return

def choose(cnt):
    #exit condition
    if len(result) == m:
        print_res()
        return

    #normal
    for x in range(cnt, n+1):
        result.append(x)
        #print("x,result,len(): %d,%s,%d" % (x,result,len(result)))
        choose(x+1)
        result.pop()
    return

choose(1)