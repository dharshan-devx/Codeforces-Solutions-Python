import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int, input().split()))

        cnt = 0

        for i in range(n - 2, -1, -1):
            while a[i] >= a[i + 1] and a[i] != 0:
                a[i] //= 2
                cnt += 1

        if any(a[i] >= a[i + 1] for i in range(n - 1)):
            print(-1)
        else:
            print(cnt)

dhxrshxn()