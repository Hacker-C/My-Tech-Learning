def Solution3(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26
    for i in s1:
        pos = ord(i) - ord('a')
        c1[pos] += 1
    for i in s2:
        pos = ord(i) - ord('a')
        c2[pos] += 1
    for i in range(26):
        if c1[i] != c2[i]:
            return False
    return True


print(Solution3('abfcda', 'acbdfa'))