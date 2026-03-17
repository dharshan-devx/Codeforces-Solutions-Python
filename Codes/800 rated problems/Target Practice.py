import sys

input = sys.stdin.read
data = input().split()

score = [
    [1,1,1,1,1,1,1,1,1,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,5,5,4,3,2,1],
    [1,2,3,4,4,4,4,3,2,1],
    [1,2,3,3,3,3,3,3,2,1],
    [1,2,2,2,2,2,2,2,2,1],
    [1,1,1,1,1,1,1,1,1,1]
]

t = int(data[0])
idx = 1

for _ in range(t):
    grid = []
    for _ in range(10):
        grid.append(data[idx])
        idx += 1

    total = 0
    for i in range(10):
        for j in range(10):
            if grid[i][j] == 'X':
                total += score[i][j]

    print(total)
