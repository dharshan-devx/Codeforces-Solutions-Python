import sys
def solve():
    input = sys.stdin.readline
    for _ in range(int(input().strip())):
        n = int(input())
        a = list(map(int, input().split()))
        
        if a[0] == 1:
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    solve()
