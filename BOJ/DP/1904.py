'''
문제
지원이에게 2진 수열을 가르쳐 주기 위해, 지원이 아버지는 그에게 타일들을 선물해주셨다. 그리고 이 각각의 타일들은 0 또는 1이 쓰여 있는 낱장의 타일들이다.

어느 날 짓궂은 동주가 지원이의 공부를 방해하기 위해 0이 쓰여진 낱장의 타일들을 붙여서 한 쌍으로 이루어진 00 타일들을 만들었다. 결국 현재 1 하나만으로 이루어진 타일 또는 0타일을 두 개 붙인 한 쌍의 00타일들만이 남게 되었다.

그러므로 지원이는 타일로 더 이상 크기가 N인 모든 2진 수열을 만들 수 없게 되었다. 예를 들어, N=1일 때 1만 만들 수 있고, N=2일 때는 00, 11을 만들 수 있다. (01, 10은 만들 수 없게 되었다.) 또한 N=4일 때는 0011, 0000, 1001, 1100, 1111 등 총 5개의 2진 수열을 만들 수 있다.

우리의 목표는 N이 주어졌을 때 지원이가 만들 수 있는 모든 가짓수를 세는 것이다. 단 타일들은 무한히 많은 것으로 가정하자.

입력
첫 번째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

출력
첫 번째 줄에 지원이가 만들 수 있는 길이가 N인 모든 2진 수열의 개수를 15746으로 나눈 나머지를 출력한다.

예제 입력 1 
4
예제 출력 1 
5
출처
문제의 오타를 찾은 사람: mwy3055
데이터를 추가한 사람: qortmd7777, wider93
'''
import sys
n=int(sys.stdin.readline().rstrip())
arr = {}
arr[0] = 0
arr[1] = 1
arr[2] = 2
def dp(m,arr):
    for i in range(3,m+1):
        arr[i] = (arr[i-1] + arr[i-2])%15746
    return arr[m]

sys.stdout.write(f"{dp(n,arr)%15746}")

'''
이게 피보나치수열 이었다니!!!??!!??!

문제의 상황에서 맨 앞에 올 수 있는 타일은 2가지 뿐입니다.

00 타일과 1 타일.

00 타일이 올 경우 00..으로 시작하고
1 타일이 올 경우 1...로 시작하겠지요.

이때 '길이가 N인 이진 수열의 개수'를 f(N)이라고 정의합시다.

그러면 경우 (1)의 가짓수는 f(N-2)가 되고 경우 (2)의 가짓수는 f(N-1)이 될 것입니다.

따라서 전체 경우의 수 f(N) 은 경우 (1) 과 (2)의 가짓수의 합인

f(N) = f(N-1) + f(N-2)가 됩니다.

또한 f(0) = f(1) = 1임을 확인할 수 있습니다.

'''
