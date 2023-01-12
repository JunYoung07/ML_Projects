# 큐의 활용
# 배열의 활용

# 시간복잡도를 활용해야 한다
# 맨앞의 값을 삭제
# 맨앞의 값을 맨 뒤로 보내기 (삭제 + 삽입)
# 삭제나 삽입의 경우 한번의 연산에서 배열에서의 시간복잡도는 O(N)
# 따라서 배열을 사용하는 것은 비효율적이다

from collections import deque

dq = deque(range(1, int(input())+1))

while len(dq) > 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq[0])