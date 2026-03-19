import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    curr = 0
    mx = 0
    for x in arr:
        if x == 0:
            curr += 1
            mx = max(mx, curr)
        else:
            curr = 0
    print(mx)