n,m,k = map(int,input().split())
distances = list(int(nums) for nums in input().split())
positions = [1]*(k+1)
result = 0


def get_score():
    global result
    score = 0
    for pos in positions:
        if pos >= m:
            score += 1
    return score

def choose(cnt):
    global result

    #update result every turn
    result = max(result, get_score())

    #exit condition
    if cnt == n:
        return

    #normal
    for player in range(1, k+1): #플레이어 중 한명선택
        #normal exception
        if positions[player] >= m:
            continue
        positions[player] += distances[cnt] #현재 턴에서 갈 수 있는 거리 더하기
        choose(cnt+1)
        positions[player] -= distances[cnt]        
    return

choose(0)
print(result)