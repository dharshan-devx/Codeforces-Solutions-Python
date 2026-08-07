import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())

        ans = 1

        for l in range(1, 61):
            cur = l

            while n % cur == 0:
                cur += 1

            ans = max(ans, cur - l)

        print(ans)

dhxrshxn()