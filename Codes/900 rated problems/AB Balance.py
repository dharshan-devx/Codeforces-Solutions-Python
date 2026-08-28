import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        s = input().strip()
        if s[0] != s[-1]:
            s = s[:-1] + s[0]
        print(s)
dhxrshxn()