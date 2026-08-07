import sys
input = sys.stdin.readline
def dhxrshxn():
    for _ in range(int(input())):
        n = int(input())
        a = input().strip()
        b = input().strip()
        odd_a = even_a = odd_b = even_b = 0
        for i in range(n):
            if a[i] == '1':
                if i % 2 == 0:
                    odd_a += 1
                else:
                    even_a += 1

            if b[i] == '1':
                if i % 2 == 0:
                    odd_b += 1
                else:
                    even_b += 1
        if odd_a == odd_b and even_a == even_b:
            print("YES")
        else:
            print("NO")
dhxrshxn()