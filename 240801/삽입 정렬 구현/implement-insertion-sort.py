a=int(input())
b=list(map(int,input().split()))

for i in range(1,a):
    j=i-1
    key=b[i]
    while j >=0 and b[j]>key:
        b[j+1]=b[j]
        j -= 1
    b[j+1]=key
for i in b:
    print(i,end=" ")

    256138
    125638
    123568