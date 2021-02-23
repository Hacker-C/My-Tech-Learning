m, n = map(int, input().split())
ac = [0] * (n + 1)
u_ac = [0] * (n + 1)
lst = []
for j in range(m):
    a, op = input().split()
    a = int(a)
    if op == 'AC':
        ac[a] += 1
    else:
        u_ac[a] += 1
    for i in range(1, n + 1):
        if i not in lst:
            if ac[i] == 0 and u_ac[i] == 0:
                pass
            elif ac[i] / (u_ac[i] + ac[i]) >= 0.5:
                print(i, end=' ')
                lst.append(i)

