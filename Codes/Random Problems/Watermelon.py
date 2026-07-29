import sys
input = sys.stdin.readline
n = int(input())
print("YES" if n % 2 == 0 and n > 2 else "No")