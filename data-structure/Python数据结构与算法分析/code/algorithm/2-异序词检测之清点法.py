def Solution1(s1, s2):
    alist = list(s2)
    pos1 = 0
    ok = True
    while pos1 < len(s1) and ok:
        pos2 = 0
        found = False
        while pos2 < len(s2) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 += 1
        pos1 += 1
        if found:
            alist[pos2] = None
        else:
            ok = False
    return ok


print(Solution1('hgtabc321145', 'cab132541ght'))
