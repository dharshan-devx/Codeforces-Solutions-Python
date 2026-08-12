import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        s = input().strip()
        curr = 1
        best = 1
        for i in range(1,n):
            if s[i] == s[i-1]:
                curr += 1
            else:
                curr = 1
            best = max(best, curr)
        print(best+1)
dhxrshxn()