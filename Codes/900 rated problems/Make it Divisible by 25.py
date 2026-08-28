import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        s = input().strip()
        ans = len(s)
        for a,b in ['00', '25', '50', '75']:
            cnt = 0
            i = len(s) - 1
            while i >= 0 and s[i] != b:
                i -= 1
                cnt += 1
            i -= 1
            
            while i >= 0 and s[i] != a:
                i -= 1
                cnt += 1
            if i >= 0:
                ans = min(ans, cnt)
        print(ans)
dhxrshxn()
            