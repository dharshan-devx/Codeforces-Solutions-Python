import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    xr = 0
    for v in arr:
        xr ^= v
    
    if n % 2 == 1:
        print(xr)
    else:
        if xr == 0:
            print(0)
        else:
            print(-1)