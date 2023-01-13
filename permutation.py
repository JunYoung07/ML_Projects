# 순열 (permutation)
# 모든 경우의 수를 순서대로 살펴볼 때 용이
# 삼성에서 next_permutation 활용하면 쉽게 풀리는 문제들이 많이 나옴

# Python Permutation
from itertools import permutations, combinations

v = [0, 1, 2, 3]

for i in permutations(v, 4):
    print(i)

# Python Combination
for i in combinations(v, 2):
    print(i)