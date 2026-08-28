t = int(input())

for _ in range(t):
    n, m, i, j = map(int, input().split())

    def dist(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    d1 = dist(i, j, 1, 1) + dist(1, 1, n, m) + dist(n, m, i, j)
    d2 = dist(i, j, 1, m) + dist(1, m, n, 1) + dist(n, 1, i, j)

    if d1 >= d2:
        print(1, 1, n, m)
    else:
        print(1, m, n, 1)