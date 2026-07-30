import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))

        arr.sort()

        if arr[0] == arr[-1]:
            print("NO")
        else:
            print("YES")
            print(arr[-1], *arr[:-1])

dhxrshxn()