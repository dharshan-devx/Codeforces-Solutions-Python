import sys

input = sys.stdin.read

data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    start = int(data[index])
    jumps = int(data[index + 1])
    index += 2

    final_pos = 0

    if jumps % 4 == 1:
        final_pos = -jumps
    elif jumps % 4 == 2:
        final_pos = 1
    elif jumps % 4 == 3:
        final_pos = jumps + 1

    if start % 2 == 0:
        final_pos = start + final_pos
    else:
        final_pos = start - final_pos

    print(final_pos)