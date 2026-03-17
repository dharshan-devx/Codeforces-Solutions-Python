import sys

def solve():
    input = sys.stdin.readline
    t = int(input())

    for _ in range(t):
        n = int(input())
        s = input().strip()

        dot_count = s.count('.')
        has_big_segment = False

        i = 0
        while i < n:
            if s[i] == '#':
                i += 1
                continue

            j = i
            while j < n and s[j] == '.':
                j += 1

            if j - i >= 3:
                has_big_segment = True

            i = j

        if dot_count == 0:
            print(0)
        elif has_big_segment:
            print(2)
        else:
            print(dot_count)

if __name__ == "__main__":
    solve()
