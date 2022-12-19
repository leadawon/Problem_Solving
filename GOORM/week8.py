#eng coding
import sys
n = int(sys.stdin.readline())
dp = [0] *(n+3)
dp[0] = 1
dp[1] = 2
dp[2] = 3

for i in range(3,n+1):
	if i%2==0:
		dp[i]=dp[i-1]+i
	else:
		dp[i]=dp[i-3]
sys.stdout.write(f"{dp[n]}")

#9+3/4
import sys
from collections import defaultdict
n,k = map(int,sys.stdin.readline().split())

isin = defaultdict(int)
timedic = defaultdict(int)

for i in range(n):
	time,name = sys.stdin.readline().split()
	if isin[name] == 0:
		h,m = map(int,time.split(":"))
		isin[name] = 60*h+m
	else:
		h,m = map(int,time.split(":"))
		if isin[name] <= 60*h+m:
			timedic[name] += 60*h+m - isin[name]
		else:
			timedic[name] += 24*60 - isin[name] + 60*h+m
		isin[name] = 0
cnt = 0
for key,val in timedic.items():

	if val >= k*60:
		cnt+=1
sys.stdout.write(f"{cnt}")
