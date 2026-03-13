import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
arr = list(map(int,data[1:]))

if 0 in arr:
    print(0)
else:
    print(min(abs(x) for x in arr))