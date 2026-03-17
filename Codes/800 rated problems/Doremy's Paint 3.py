import sys
from collections import Counter

data = sys.stdin.read().split()
idx = 0

t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    idx += 1
    
    a = list(map(int, data[idx:idx + n]))
    idx += n
    
    freq = Counter(a)

    if len(freq) == 1:
        print("Yes")
    elif len(freq) == 2:
        c1, c2 = freq.values()
        if abs(c1 - c2) <= 1:
            print("Yes")
        else:
            print("No")
    else:
        print("No")
