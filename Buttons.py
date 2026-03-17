import sys
input = sys.stdin.readline
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    anna = a + (c + 1) // 2
    katie = b + c // 2
    if anna > katie:
        print("First")
    else:
        print("Second")