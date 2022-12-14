'''
문제
n개의 정수로 이루어진 임의의 수열이 주어진다. 우리는 이 중 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중 가장 큰 합을 구하려고 한다. 단, 수는 한 개 이상 선택해야 한다.

예를 들어서 10, -4, 3, 1, 5, 6, -35, 12, 21, -1 이라는 수열이 주어졌다고 하자. 여기서 정답은 12+21인 33이 정답이 된다.

입력
첫째 줄에 정수 n(1 ≤ n ≤ 100,000)이 주어지고 둘째 줄에는 n개의 정수로 이루어진 수열이 주어진다. 수는 -1,000보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 답을 출력한다.

예제 입력 1 
10
10 -4 3 1 5 6 -35 12 21 -1
예제 출력 1 
33
예제 입력 2 
10
2 1 -4 3 4 -4 6 5 -5 1
예제 출력 2 
14
예제 입력 3 
5
-1 -2 -3 -4 -5
예제 출력 3 
-1
출처
데이터를 추가한 사람: djm03178, dohyeokkim, doju, jh05013, kimdr123, seedkin
빠진 조건을 찾은 사람: isac322, Qwaz
문제의 오타를 찾은 사람: jh05013
잘못된 데이터를 찾은 사람: tncks0121
'''
import sys
#sys.stdin = open("testcase.txt","r")
n = int(sys.stdin.readline().rstrip())
arr = [-1000] *n

for i,v in enumerate(map(int,sys.stdin.readline().split())):
    if i == 0:
        arr[0] = v
    arr[i] = max(arr[i-1] + v, v)
sys.stdout.write(f"{max(arr)}")
'''
자꾸 dp문제 풀때 비효율적으로 생각함...
음수가 나올때 그 음수를 다시 양수로 채우기 위해서 필요한 만큼 채우려면
음수 전까지의 최댓값에 음수를 더한 값으로 채워나가면 되는 것이다.
'''
