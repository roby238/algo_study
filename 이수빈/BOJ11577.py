inp = list(map(int, input().split()))
N = inp[0]
K = inp[1]
bulbs = list(map(int, input().split()))
switch_cnt = [0] * (N + 1)
count = 0

for i in range(N):
    switch_cnt[i] += switch_cnt[i-1] if i > 0 else 0
    bulbs[i] = bulbs[i] ^ 1 if switch_cnt[i] % 2 == 1 else bulbs[i]
    if bulbs[i] == 1:
        if i + K > N:
            count = -1
            break
        else:
            switch_cnt[i] += 1
            switch_cnt[i+K] += 1
            bulbs[i] = bulbs[i] ^ 1
            count += 1

print("Insomnia" if count == -1 else count)
 