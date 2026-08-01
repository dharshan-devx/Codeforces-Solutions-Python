import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        s = input().strip()

        freq = [0] * 26

        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        odd = 0
        for f in freq:
            if f % 2:
                odd += 1

        if max(0, odd - 1) <= k:
            print("YES")
        else:
            print("NO")

dhxrshxn()




