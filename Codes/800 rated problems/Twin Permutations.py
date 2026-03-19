import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    
    q = [n + 1 - x for x in arr]
    print(*q)