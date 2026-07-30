import sys
input = sys.stdin.readline

def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        
        digits = len(str(n))
        power = 10**(digits-1)
        print(9*(digits-1)+n//power)
dhxrshxn()





