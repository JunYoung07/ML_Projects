'''import sys
import queue

Q = queue.Queue()
Q.put(i for i in range(1, int(sys.stdin.readline())+1))

while not Q.qsize() == 1:
    Q.get()
    Q.put(Q.get())

print(Q.get())'''

'''import sys

Q = [i for i in range(1, int(sys.stdin.readline())+1)]

while len(Q) != 1:
    Q.pop(0)
    Q.append(Q.pop(0))

print(Q[0]) '''

from collections import deque
import sys

dq = deque([i for i in range(int(sys.stdin.readline()), 0,-1)])

while len(dq) != 1:
    dq.pop()
    dq.appendleft(dq.pop())
    # print(dq)

print(dq[0])