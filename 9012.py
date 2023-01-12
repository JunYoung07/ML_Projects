import sys
# sys.stdin.readline()
n = int(input())
answer = []

for _ in range(n):
    stk = []
    par = sys.stdin.readline()
    for item in par:
        if item == '(':
            stk.append(item)
        elif item == ')':
            if len(stk)==0:
                stk.append(1)
            else:
                if stk[-1] == '(':
                    stk.pop()
                else:
                    pass
        # print(stk)
    
    if len(stk) == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for ans in answer:
    print(ans)
    

