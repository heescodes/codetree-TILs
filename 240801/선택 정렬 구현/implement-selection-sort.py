a=int(input())
b=list(map(int,input().split()))

for i in range(a):
    minimum=i
    for j in range(i+1,a):
        if b[j] < b[minimum]:
            minimum = j
    tmp = b[i]
    b[i] = b[minimum]
    b[minimum] = tmp

for i in b:
    print(i,end = " ")