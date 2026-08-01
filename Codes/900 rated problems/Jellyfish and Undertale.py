import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        a,b,n = map(int,input().split())
        arr = list(map(int,input().split()))
        ans = b
        for x in arr:
            ans += min(x, a - 1)
        print(ans)
dhxrshxn()
        