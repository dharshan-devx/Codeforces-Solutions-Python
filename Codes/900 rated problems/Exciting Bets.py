import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        a,b = map(int,input().split())
        d = abs(a-b)
        if d == 0:
            print(0,0)
            continue    
        moves = min(a % d, d - (a % d))
        print(d, moves)
dhxrshxn()