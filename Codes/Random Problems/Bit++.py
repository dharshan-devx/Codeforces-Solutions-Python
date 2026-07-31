import sys
input = sys.stdin.readline
def dhxrshxn():
    n = int(input())
    cnt = 0
    for _ in range(n):
        state = input()
        if "++" in state:
            cnt += 1
        else:
            cnt -= 1
    print(cnt)

dhxrshxn()