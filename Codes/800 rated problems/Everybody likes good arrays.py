import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        
        ans = 0
        cnt = 1
        for i in range(1,n):
            if arr[i] % 2 == arr[i-1] % 2:
                cnt += 1
            else:
                ans += cnt - 1
                cnt = 1
        ans += cnt - 1
        print(ans)
dhxrshxn()