import sys
n,m,k = map(int,sys.stdin.readline().split())

arr=[[0 for _ in range(m)] for _ in range(n)]
row=0
col=0
arr[row][col] = 1
max1 = 0
for i in range(k):
	c = sys.stdin.read(1)
	
	if c=="N":
		if row==0:
			arr[row][col] += 1
		else:
			row -= 1
			arr[row][col] += 1
		if arr[row][col] > max1:
				max1 = arr[row][col]
	elif c=="W":
		if col == m-1:
			arr[row][col] += 1
		else:
			col += 1
			arr[row][col] += 1
		if arr[row][col] > max1:
				max1 = arr[row][col]
	elif c=="S":
		if row == n-1:
			arr[row][col] += 1
		else:
			row += 1
			arr[row][col] += 1
		if arr[row][col] > max1:
				max1 = arr[row][col]
	elif c=="E":
		if col == 0:
			arr[row][col] += 1
		else:
			col -= 1
			arr[row][col] += 1
		if arr[row][col] > max1:
				max1 = arr[row][col]


sys.stdout.write(str(max1))
