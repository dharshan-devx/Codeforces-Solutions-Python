import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        ans = a[0]
        for i in range(1, n):
            ans = ans & a[i]
        print(ans)
dhxrshxn()