'''
문제
도현이의 집 N개가 수직선 위에 있다. 각각의 집의 좌표는 x1, ..., xN이고, 집 여러개가 같은 좌표를 가지는 일은 없다.

도현이는 언제 어디서나 와이파이를 즐기기 위해서 집에 공유기 C개를 설치하려고 한다. 최대한 많은 곳에서 와이파이를 사용하려고 하기 때문에, 한 집에는 공유기를 하나만 설치할 수 있고, 가장 인접한 두 공유기 사이의 거리를 가능한 크게 하여 설치하려고 한다.

C개의 공유기를 N개의 집에 적당히 설치해서, 가장 인접한 두 공유기 사이의 거리를 최대로 하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 개수 N (2 ≤ N ≤ 200,000)과 공유기의 개수 C (2 ≤ C ≤ N)이 하나 이상의 빈 칸을 사이에 두고 주어진다. 둘째 줄부터 N개의 줄에는 집의 좌표를 나타내는 xi (0 ≤ xi ≤ 1,000,000,000)가 한 줄에 하나씩 주어진다.

출력
첫째 줄에 가장 인접한 두 공유기 사이의 최대 거리를 출력한다.

예제 입력 1 
5 3
1
2
8
4
9
예제 출력 1 
3
'''
import sys
#sys.stdin = open("testcase.txt","r")
n,c = map(int, sys.stdin.readline().split())
arr = []
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))

arr = sorted(arr)
start = 1
end = arr[-1] - arr[0]
ans = 0
while start <= end:
    mid = (start + end) // 2
    cnt = 1
    current = arr[0]
    for i in range(1,len(arr)):
        if arr[i] >= current + mid:
            cnt += 1
            current = arr[i]

    if cnt >= c:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
print(ans)
'''
start 와 end로 while문의 종료조건 설정.
여기서 start는 집 사이 거리의 최솟값의 의미로 일단 임의로 1로 설정.
end는 집 사이 거리의 최댓값으로 정렬 후 수직선에서 가장 먼 집과 가장 가까운 집의 위치를 뺀다.
집과 집사이는 start와 end 사이에서 벗어날 수 없다.
집과 집사이에 대해서 이진 탐색을 실시한다.

처음 집은 항상 공유기를 둘 수 밖에 없다.
두번째 혹은 세번째 집부터 공유기를 둔다고 가정하면
그곳에 둘 공유기는 첫번째 집에다 두면 더 먼거리로 설정할 수 있기 때문이다.

mid를 계속 초기화 해주면서 while문을 돈다. cnt가 c보다 크거나 같다는 것은 거리를 너무 작게 설정해서
더 큰거리로 둘 수 있는 상황이므로 mid+1값이 start가 된다.

cnt가 c보다 작다는 것은 공유기간 거리를 너무 크게 설정해서 공유기 설치 횟수에 못미치는 것이다.
이때는 공유기간 거리를 더 작게 한다.
'''
