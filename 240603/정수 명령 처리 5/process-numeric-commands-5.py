n = int(input())
vector = []
try:
    while 1:
        command = input()
        if 'push_back' in command:
            vector.append(int(command.split()[1]))
        elif 'pop_back' in command:
            vector.pop()
        elif 'size' in command:
            print(len(vector))
        elif 'get' in command:
            print(vector[int(command.split()[1])-1])
except:
    pass