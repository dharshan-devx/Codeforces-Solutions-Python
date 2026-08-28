import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        a,b,c = map(int,input().split())
        
        if (2 * b - c) > 0 and (2 * b - c) % a == 0:
            print("YES")
        elif (a + c) % (2 * b) == 0:
            print("YES")
        elif (2 * b - a) > 0 and (2 * b - a) % c == 0:
            print("YES")
        else:
            print("NO")
dhxrshxn()  