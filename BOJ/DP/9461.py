'''
문제
오른쪽 그림과 같이 삼각형이 나선 모양으로 놓여져 있다. 첫 삼각형은 정삼각형으로 변의 길이는 1이다. 그 다음에는 다음과 같은 과정으로 정삼각형을 계속 추가한다. 
나선에서 가장 긴 변의 길이를 k라 했을 때, 그 변에 길이가 k인 정삼각형을 추가한다.

파도반 수열 P(N)은 나선에 있는 정삼각형의 변의 길이이다. P(1)부터 P(10)까지 첫 10개 숫자는 1, 1, 1, 2, 2, 3, 4, 5, 7, 9이다.

N이 주어졌을 때, P(N)을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. (1 ≤ N ≤ 100)

출력
각 테스트 케이스마다 P(N)을 출력한다.

예제 입력 1 
2
6
12
예제 출력 1 
3
16
출처
ICPC > Regionals > Asia Pacific > Korea > Asia Regional - Daejeon 2013 G번

문제를 번역한 사람: baekjoon
문제의 오타를 찾은 사람: eric00513
'''
import sys
from collections import defaultdict
# 1 1 1 2 2 3 // 4 5 7  9 12 16 21
'''
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = p[1] + p[3] = 2
p[5] = p[4] = 2
p[6] = p[1] + p[5] = 3
p[7] = p[2] + p[6] = 4
p[8] = p[3] + p[7] = 5
p[9] = p[4] + p[8] = 7
p[10] = p[5] + p[9] = 9
p[11] = p[6] + p[10] = 12
p[12] = p[7] + p[11] = 16
'''
p = defaultdict(int)
p[1] = 1
p[2] = 1
p[3] = 1
p[4] = p[1] + p[3]# = 2
p[5] = p[4]# = 2
t=int(sys.stdin.readline().rstrip())
mem = 6
for i in range(t):
    n = int(sys.stdin.readline().rstrip())
    if p[n] != 0:
        sys.stdout.write(f"{p[n]}\n")
    else:
        for j in range(mem,n+1):
            p[j] = p[j-5] + p[j-1]
        mem = n+1
        sys.stdout.write(f"{p[n]}\n")
        
'''
직접 수열을 적어보면서 규칙을 알아냈다.
dp를 사용했다.
'''
