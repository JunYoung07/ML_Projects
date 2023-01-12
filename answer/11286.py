# 우선순위 큐
import heapq as hq
import sys

# 코딩테스트에 있어 빠른 입출력을 사용해야 하는 상황도 고려를 해야한다
input = sys.stdin.readline
pq = []
for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x), x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)

# 2번째 방법
'''
min_heap = [] # 양수
max_heap = [] # 음수
for _ in range(int(input())):
    x = int(input())
    if x:
        if x > 0:
            hq.heappush(min_heap, x)
        else:
            hq.heappush(max_heap, -x)
    else:
        if min_heap:
            if max_heap:
                if min_heap[0] < abs(max_heap[0]):
                    print(hq.heappop(min_heap))
                else:
                    print(-hq.heappop(min_heap))
            else:
                print(hq.heappop(min_heap))
        else:
            if max_heap:
                print(-hq.heappop(max_heap))
            else:
                print(0)
'''