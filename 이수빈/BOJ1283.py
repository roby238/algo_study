n = int(input())
key = set()

for i in range(n):
    l = input().split(' ')
    idx = 0
    key_check = 1
    while idx < len(l):
        if l[idx][0].lower() not in key:
            key.add(l[idx][0].lower())
            key_check = 0
            break
        idx += 1

    if key_check:
        key_n = 0
        for i in range(len(l)):
            for j in range(len(l[i])):
                if l[i][j].lower() not in key and not key_n:
                    print(f"[{l[i][j]}]", end='')
                    key.add(l[i][j].lower())
                    key_n = 1
                else:
                    print(l[i][j], end='')
            print(" ", end='')
            
    else:
        for i in range(len(l)):
            if i == idx:
                print(f"[{l[i][0]}]{l[i][1:]} ", end='')
            else:
                print(l[i], end=' ')
    print()