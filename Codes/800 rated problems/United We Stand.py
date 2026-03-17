


import sys

input = sys.stdin.read

data = input().split()

index = 0

t = int(data[index]) 
index += 1

for _ in range(t):
	n = int(data[index]) 
	index += 1
	a = list(map(int, data[index:index + n])) 
	index += n


	mx = max(a)
	b = [] 
	c = [] 


	for value in a:
		if value != mx:
			b.append(value) 
		else:
			c.append(value) 
	if len(b) == 0:
		print(-1) 
	else:
		print(len(b), len(c))
		print(' '.join(map(str, b)))
		print(' '.join(map(str, c)))