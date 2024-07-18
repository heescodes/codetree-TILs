c = int(input())
my_list = []
while c != 0:
    command = input()
    if command == "size":
        print(len(my_list))
    elif command.split()[0] == "push_back":
        my_list.append(command.split()[1])
    elif command.split()[0] == "pop_back":
        my_list.pop()
    elif command.split()[0] == "get":
        print(my_list[int(command.split()[1])-1])
    c -=1