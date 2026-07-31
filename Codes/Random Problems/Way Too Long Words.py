import sys
input = sys.stdin.readline

def dhxrshxn():
    n = int(input())
    for _ in range(n):
        words = input().strip()
        if len(words) > 10:
            print(words[0] + str(len(words) -2) + words[-1])
        else:
            print(words)
dhxrshxn()