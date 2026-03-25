import sys
input = sys.stdin.read
data = input().split()
t = int(data[0])
index = 1
for _ in range(t):
	n = int(data[index])
	a = int(data[index + 1])
	b = int(data[index + 2])
	index += 3
	if a + b + 2 <= n or (a == b and a == n):
		print("Yes")  
	else:
		print("No")  