import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        a = input().strip()
        b = input().strip()
        pos_a_odd = []
        pos_a_even = []
        pos_b_odd = []
        pos_b_even = []
        for i in range(n):
            if a[i] == '1':
                if i & 1:
                    pos_a_even.append(i)
                else:
                    pos_a_odd.append(i)
            if b[i] == '1':
                if i & 1:
                    pos_b_even.append(i)
                else:
                    pos_b_odd.append(i)
        if len(pos_a_odd) != len(pos_b_odd) or len(pos_a_even) != len(pos_b_even):
            print(-1)
            continue
        ans = 0
        for x, y in zip(pos_a_odd, pos_b_odd):
            ans += abs(x - y) // 2
        for x, y in zip(pos_a_even, pos_b_even):
            ans += abs(x - y) // 2
        print(ans)
dhxrshxn()