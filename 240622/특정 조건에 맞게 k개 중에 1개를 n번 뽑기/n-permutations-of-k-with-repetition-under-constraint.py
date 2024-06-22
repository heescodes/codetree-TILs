answer = []
k, n = map(int, input().split())


def print_ans():
    for x in answer:
        print(x, end = " ")
    print()

def choose(cur_num):
    #exit condition
    if cur_num == n+1:
        print_ans()
        return

    #normal case
    for i in range(1, k+1):
        answer.append(i)
        if cur_num == 1 or cur_num == 2 or not(answer[-1] == answer[-2] == answer[-3]):
            choose(cur_num + 1)
        answer.pop()
    
    return


choose(1)