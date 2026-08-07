import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        r = 1
        for i in range(1, n):
            if s[i] != s[i - 1]:
                r += 1
        ans = r
        for i in range(1, n - 1):
            t1 = 1 if s[i - 1] != s[i] else 0
            t2 = 1 if s[i] != s[i + 1] else 0
            t3 = 1 if s[i - 1] != s[i + 1] else 0
            ans = min(ans, r - t1 - t2 + t3)
        print(ans)
dhxrshxn()