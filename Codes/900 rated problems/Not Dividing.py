import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        for i in range(n):
            if arr[i] == 1:
                arr[i] += 1

            if i > 0 and arr[i] % arr[i - 1] == 0:
                arr[i] += 1

        print(*arr)

dhxrshxn()