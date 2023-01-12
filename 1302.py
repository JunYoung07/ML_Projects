import sys

# input = sys.stdin.readline
lst = dict()
ans = []
for _ in range(int(input())):
    name = input()
    if name not in lst.keys():
        lst[name] = 1
    else:
        lst[name] += 1

lst = sorted(lst.items(), key=lambda x:x[1], reverse=True)
for x in lst:
    if x[1] == lst[0][1]:
        ans.append(x)
    else:
        break
# lst.sort()
ans.sort()
print(ans[0][0])
