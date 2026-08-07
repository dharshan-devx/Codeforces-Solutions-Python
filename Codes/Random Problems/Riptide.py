import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        a, b, c = map(int, input().split())
        ans = 0

        while len({a, b, c}) == 3:
            arr = [(a, 0), (b, 1), (c, 2)]
            arr.sort()

            vals = [a, b, c]
            vals[arr[0][1]] += 1
            vals[arr[2][1]] -= 1

            a, b, c = vals
            ans += 1

        print(ans)

dhxrshxn()