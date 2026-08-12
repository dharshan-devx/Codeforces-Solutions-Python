import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        a = list(map(int,input().split()))
        ans = 0
        for i in range(n):
            if a[i] != 0 and (i==0 or a[i-1] == 0):
                ans += 1
        print(min(ans,2))
        
        
dhxrshxn()