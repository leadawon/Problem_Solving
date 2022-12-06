'''
문제
지민이는 N개의 원소를 포함하고 있는 양방향 순환 큐를 가지고 있다. 지민이는 이 큐에서 몇 개의 원소를 뽑아내려고 한다.

지민이는 이 큐에서 다음과 같은 3가지 연산을 수행할 수 있다.

첫 번째 원소를 뽑아낸다. 이 연산을 수행하면, 원래 큐의 원소가 a1, ..., ak이었던 것이 a2, ..., ak와 같이 된다.
왼쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 a2, ..., ak, a1이 된다.
오른쪽으로 한 칸 이동시킨다. 이 연산을 수행하면, a1, ..., ak가 ak, a1, ..., ak-1이 된다.
큐에 처음에 포함되어 있던 수 N이 주어진다. 그리고 지민이가 뽑아내려고 하는 원소의 위치가 주어진다. (이 위치는 가장 처음 큐에서의 위치이다.) 이때, 그 원소를 주어진 순서대로 뽑아내는데 드는 2번, 3번 연산의 최솟값을 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 큐의 크기 N과 뽑아내려고 하는 수의 개수 M이 주어진다. N은 50보다 작거나 같은 자연수이고, M은 N보다 작거나 같은 자연수이다. 둘째 줄에는 지민이가 뽑아내려고 하는 수의 위치가 순서대로 주어진다. 위치는 1보다 크거나 같고, N보다 작거나 같은 자연수이다.

출력
첫째 줄에 문제의 정답을 출력한다.

예제 입력 1 
10 3
1 2 3
예제 출력 1 
0
예제 입력 2 
10 3
2 9 5
예제 출력 2 
8
예제 입력 3 
32 6
27 16 30 11 6 23
예제 출력 3 
59
예제 입력 4 
10 10
1 6 3 2 7 9 8 4 10 5
예제 출력 4 
14
'''
import sys
from collections import deque

sys.stdin = open("testcase.txt","r")

n,m = map(int,sys.stdin.readline().split())
arr = [i for i in range(n)]
arr = deque(arr)
front = 0
cnt = 0
for cmd in map(int,sys.stdin.readline().split()):
    cmd = cmd-1
    if arr[front] == cmd:
        del arr[front]
        if front == n - 1:
            front = 0
        n -= 1
        continue
    lfront=front
    rfront=front
    while True:
        if lfront == 0:
            lfront = n-1
        else:
            lfront -= 1
        if rfront == n-1:
            rfront = 0
        else:
            rfront += 1
        cnt += 1
        if arr[lfront] == cmd:
            del arr[lfront]
            if lfront == n - 1:
                front = 0
            else:
                front = lfront
            n -= 1
            break
        elif arr[rfront] == cmd:
            del arr[rfront]
            if rfront == n - 1:
                front = 0
            else:
                front = rfront
            n -= 1
            break
sys.stdout.write(f"{cnt}")

'''
front와 rear이 있을때
front에서 pop을 실행한다.
왼쪽으로 민다는 것은 front를 앞으로 rear도 앞으로
오른쪽으로 민다는 것은 front를 뒤로 rear도 뒤로....

front 포인터만 다루고 front가 해당 값을 찾을 때까지 2,3연산을 한다.
front포인터가 가리키는 값이 해당 값과 동일하면 delete한다.
'''
