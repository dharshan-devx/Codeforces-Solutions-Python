import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        l = 0
        r = n - 1
        while l < r and s[l] != s[r]:
            l += 1
            r -= 1
        print(r-l+1)
dhxrshxn()