def Solution2(s1, s2):
    list1 = list(s1)
    list2 = list(s2)
    list1.sort()
    list2.sort()
    pos = -1
    ok = True
    while (pos := pos+1) < len(s1) and ok:
        if list1[pos] != list2[pos]:
            ok = False
    return ok


print(Solution2('ab2c1d3', '123cbda'))