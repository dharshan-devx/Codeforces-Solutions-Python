import math
import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    p = list(map(int, input().split()))

    g = 0
    for i, x in enumerate(p, 1):
        g = math.gcd(g, abs(i - x))

    print(g)