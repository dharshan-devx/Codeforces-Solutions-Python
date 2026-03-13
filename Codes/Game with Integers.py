import sys

def solve():
    input = sys.stdin.readline
    for _ in range(int(input().strip())):
        n = int(input().strip())
        if n % 3 == 0:
            print("Second")
        else:
            print("First")
solve()
