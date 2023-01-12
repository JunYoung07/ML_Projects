# 우선순위큐
from queue import PriorityQueue
import sys

que = PriorityQueue()

n = int(sys.stdin.readline())
for _ in range(n):
    k = int(sys.stdin.readline())
    if k == 0:
        if que.qsize() == 0:
            print(0)
        else:
            print(que.get()[1])
    else:
        que.put((abs(k), k))