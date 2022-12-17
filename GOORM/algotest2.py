#kiyak
import sys
import math
n = int(sys.stdin.readline().rstrip())
a=1
b=n-1
suma = 0
for i in range(n):
	if a > b:
		break
	if math.gcd(a,b)==1:
		suma += 1
	a += 1
	b -= 1
sys.stdout.write(f"{suma}")

#9ketmon
import sys
n,m = map(int,sys.stdin.readline().split())
cnt = 0
arr = [0] * n
ans = -1
for i in range(m):
	st = int(sys.stdin.readline().rstrip()) - 1
	if arr[st] == 0:
		arr[st] = 1
		cnt += 1
	if cnt == n:
		ans = i+1
		break
else:
	ans = -1	

sys.stdout.write(f"{ans}")

#fibonacci
import sys
import bisect
t = int(sys.stdin.readline().rstrip())

dp = [0]*50
dp[0] = 0
dp[1] = 1

suma = [0]*50
suma[0] = -1
suma[1] = 1

maxind = 1
for i in range(t):
	n = int(sys.stdin.readline().rstrip())
	if suma[maxind] < n:
		while suma[maxind] < n:
			dp[maxind+1] = dp[maxind] + dp[maxind-1]
			suma[maxind+1] = suma[maxind]+dp[maxind+1]
			maxind += 1
		sys.stdout.write(f"{maxind-1}\n")
	else:
		finded = bisect.bisect_left(suma[:maxind+1],n)
		sys.stdout.write(f"{finded-1}\n")

#boom
import sys
n,m,k = map(int,sys.stdin.readline().split())
arr = []
stac = []
for i in range(n):
	arr.append(list(map(int,sys.stdin.readline().split())))
for i in range(k):
	x,y=map(int,sys.stdin.readline().split())
	if arr[x-1][y-1] == 0 or m==0:
		continue
	stac.append((x-1,y-1))
	while stac:
		item = stac.pop()
		boom = arr[item[0]][item[1]]
		arr[item[0]][item[1]] = 0
		m-=1
		if m==0:
			break
		for row in range(max(0,item[0]-boom),min(n-1,item[0]+boom)+1):
			if row==item[0]:
				for col in range(max(0,item[1]-boom),min(n-1,item[1]+boom)+1):
					if arr[row][col] > 0:
						stac.append((row,col))
			else:
				if arr[row][item[1]] > 0:
					stac.append((row,item[1]))
sys.stdout.write(f"{m}")
					
