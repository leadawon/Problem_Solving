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

#
