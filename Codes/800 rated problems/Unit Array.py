import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    neg = arr.count(-1)
    pos = arr.count(1)
    cnt = 0
    
    while neg > pos:
        neg -= 1
        pos += 1
        cnt += 1
    if neg % 2 == 1:
        cnt += 1
    print(cnt)
    