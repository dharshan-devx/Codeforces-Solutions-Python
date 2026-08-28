import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int,input().split()))
        ans = 0
        ones = arr.count(1)
        zeros = arr.count(0)
        if ones == 0:
            print(0)
            continue
        ans = ones * 2**zeros
        print(ans)
        
dhxrshxn()        