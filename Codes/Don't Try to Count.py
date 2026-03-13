import sys

data = sys.stdin.read().split()
idx = 0
t = int(data[idx]); idx += 1

for _ in range(t):
    n = int(data[idx])
    m = int(data[idx+1])
    idx += 2

    x = data[idx]
    s = data[idx+1]
    idx += 2

    cur = x
    ans = -1

    for k in range(6):
        if s in cur:
            ans = k
            break
        cur += cur

    print(ans)
