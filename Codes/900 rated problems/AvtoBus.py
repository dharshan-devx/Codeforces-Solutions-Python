import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        if n < 4 or n % 2 != 0:
            print(-1)
            continue
        mini = (n+5) // 6
        maxi = n // 4
        print(mini, maxi)
dhxrshxn()