from collections import Counter

t = int(input())

for _ in range(t):
    s, target = input().split()

    need = Counter(target)
    ans = []
    for ch in reversed(s):
        if need[ch] > 0:
            ans.append(ch)
            need[ch] -= 1
    ans.reverse()

    if ''.join(ans) == target:
        print("YES")
    else:
        print("NO")