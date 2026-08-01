import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        a,b = map(int,input().split())
        xk,yk = map(int,input().split())
        xq,yq = map(int,input().split())
        moves = {
            (a,b),
            (a,-b),
            (-a,b),
            (-a,-b),
            
            (b,a),
            (b,-a),
            (-b,a),
            (-b,-a)
        }
        king = set()
        queen = set()
        for dx,dy in moves:
            king.add((xk + dx, yk + dy))
            queen.add((xq + dx, yq + dy))
        ans = king & queen
        print(len(ans))
dhxrshxn()