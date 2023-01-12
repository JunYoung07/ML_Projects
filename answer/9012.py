# stack 활용
for _ in range(int(input())):
    stk = []
    isVPS = True
    for ch in input():
        if ch == '(':
            stk.append(ch)
        else:
            if len(stk) == 0:
                isVPS = False
                break
            stk.pop()

    if len(stk) > 0:
        isVPS = False

    print('YES' if isVPS else 'NO')