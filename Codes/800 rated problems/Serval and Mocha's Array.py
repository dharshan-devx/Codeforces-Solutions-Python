import sys
from math import gcd
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        ok = False
        for i in range(n):
            for j in range(i + 1, n):
                if gcd(arr[i], arr[j]) <= 2:
                    ok = True
                    break
            if ok:
                break
        print("Yes" if ok else "No")
dhxrshxn()