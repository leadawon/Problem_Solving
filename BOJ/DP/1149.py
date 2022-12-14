'''
문제
RGB거리에는 집이 N개 있다. 거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

집은 빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다. 각각의 집을 빨강, 초록, 파랑으로 칠하는 비용이 주어졌을 때, 아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자.

1번 집의 색은 2번 집의 색과 같지 않아야 한다.
N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
입력
첫째 줄에 집의 수 N(2 ≤ N ≤ 1,000)이 주어진다. 둘째 줄부터 N개의 줄에는 각 집을 빨강, 초록, 파랑으로 칠하는 비용이 1번 집부터 한 줄에 하나씩 주어진다. 집을 칠하는 비용은 1,000보다 작거나 같은 자연수이다.

출력
첫째 줄에 모든 집을 칠하는 비용의 최솟값을 출력한다.

예제 입력 1 
3
26 40 83
49 60 57
13 89 99
예제 출력 1 
96
예제 입력 2 
3
1 100 100
100 1 100
100 100 1
예제 출력 2 
3
예제 입력 3 
3
1 100 100
100 100 100
1 100 100
예제 출력 3 
102
예제 입력 4 
6
30 19 5
64 77 64
15 19 97
4 71 57
90 86 84
93 32 91
예제 출력 4 
208
예제 입력 5 
8
71 39 44
32 83 55
51 37 63
89 29 100
83 58 11
65 13 15
47 25 29
60 66 19
예제 출력 5 
253
'''
import sys

def argmin(arr,noind=-1):
    min1 = 1000
    ind = 0
    for i in range(len(arr)):
        if min1 > arr[i] and noind!=i:
            min1 = arr[i]
            ind = i
    return min1,ind

sys.stdin = open("testcase.txt","r")
n = int(sys.stdin.readline().rstrip())
rgb = []
for i in range(n):
    rgb.append(list(map(int,sys.stdin.readline().split())))

r = [0] *n
g = [0] *n
b = [0] *n

r[0] = rgb[0][0]
g[0] = rgb[0][1]
b[0] = rgb[0][2]

for i in range(1,n):
    r[i] = min(g[i - 1], b[i - 1]) + rgb[i][0]
    g[i] = min(r[i - 1], b[i - 1]) + rgb[i][1]
    b[i] = min(g[i - 1], r[i - 1]) + rgb[i][2]
sys.stdout.write(f"{min(r[n-1],g[n-1],b[n-1])}")





'''
DP의 전형적인 풀이 방식이라 생각하는데, 답을 구하기 위해 필요한 정보를 역으로 추적해나가는 과정이라 생각합니다.

먼저, 구하고자 하는 답은 1번 집부터 N번 집까지 색칠하는 비용의 최솟값입니다. 그러니, f(x) = "1번 집부터 x번 집까지 색칠하는 비용의 최솟값" 으로 정의합시다.

이제 f(x)를 f(x-1), f(x-2) 등등의 이전 함숫값으로부터 구하려면 어떻게 해야 할지 생각해야 하는데... 당장 잘 떠오르진 않습니다. 색깔에 대한 정보가 식에 포함되어야 할 것 같은데 당장 만들어둔 f의 정의는 그런게 없네요.

f에 대해 조금 더 생각해봅니다. N개의 집에 색을 어떻게 칠하든, 마지막 집의 색을 R, G, B 세 종류 중 하나로 칠했을 겁니다. 각각의 경우마다 비용을 따로 모아볼 수 있을텐데, 전체의 최솟값 (= f)은 마지막 집 색을 R로 고정하고 비용을 최소로 한 경우이거나, 아니면 G/B로 고정하고 마찬가지로 구한 세 경우 중 하나여야 합니다.

이를 생각의 흐름을 식으로 풀어봅시다.

마지막 집의 색을 R/G/B로 고정했을 때 1~x까지의 집을 색칠하는 비용의 최솟값을 각각 r(x), g(x), b(x)라 한다면 다음이 성립합니다.

f(x) = min(r(x), g(x), b(x))

f 하나만 생각해도 벅찬데, 굳이 r, g, b를 꺼낸 이유는 색깔 정보를 포함해야 점화식을 세울 수 있다고 생각했기 때문입니다.

그러면 r(x), g(x), b(x)를 r(x-1), g(x-1), b(x-1), ... 의 이전 정보로부터 구할 방법이 있을까요?

이제는 있습니다.

이웃한 집의 색이 달라야 하니, 마지막 집의 색이 R이었다면 그 직전 집의 색은 G 혹은 B겠네요. 이걸 바탕으로 식을 세우면,

r(x) = min(g(x-1), b(x-1)) + (마지막 집을 R로 칠하는데 든 비용) 이겠네요.

마찬가지로 g(x), b(x)도 식을 세울 수 있겠습니다.

이런 식으로 상황을 나누어 점화식을 구하는 테크닉은 정말 많이 쓰이고, 고수들이 이런 문제를 빠르게 풀 수 있는 이유는 첫째로 이러한 테크닉의 사용에 익숙하며, 둘째로 많이 접해봤기 때문입니다.

답변이 도움이 되셨길 바랍니다.

<https://www.acmicpc.net/board/view/101509>
'''
