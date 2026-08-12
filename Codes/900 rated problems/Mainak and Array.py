import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        ans = a[-1] - a[0]
        ans = max(ans, max(a) - a[0])
        ans = max(ans, a[-1] - min(a))
        for i in range(n-1):
            ans = max(ans,a[i] - a[i+1])
        print(ans)             
dhxrshxn()