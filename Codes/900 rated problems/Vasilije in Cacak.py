import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n,k,x = map(int,input().split())
        
        mini = k * (k + 1) // 2
        maxi = k * (2 * n - k + 1) // 2
        if mini <= x <= maxi:
            print("YES")
        else:
            print("NO")
        
        
        
dhxrshxn()