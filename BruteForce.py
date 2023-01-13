# n개의 수를 입력받아 두 수를 뽑아 합이 가장 클 때
lst = list(map(int, input().split()))
ans = []

for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        ans.append(lst[i]+lst[j])

print(max(ans))

# 하지만 브루트 포스방식은 시간이 2초 입력이 N<=1000000인 경우에 사용할 수 없다 (O(N^2))

# 효율적인 방법
# 정렬을 이용한다 (O(NlogN))
lst.sort(reverse=True)
print(lst[0]+lst[1])