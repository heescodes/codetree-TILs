a=input()
b=input()
my_list = list(map(int,b.split()))
sorted = False

while sorted == False:
    sorted = True
    for i in range(int(a)-1):
        if my_list[i] > my_list[i+1]:
            tmp = my_list[i]
            my_list[i] = my_list[i+1]
            my_list[i+1] = tmp
            sorted = False
for i in my_list:
    print(i,end=" ")