import sys
input = sys.stdin.readline

for _ in range(int(input())):
    a,b,c,d = map(int,input().split())
    
    if d < b:
        print(-1)
        continue
    
    x_after_diag = a + (d - b)
    
    if x_after_diag < c:
        print(-1)
        continue
    
    ans = (d - b) + (x_after_diag - c)
    print(ans)