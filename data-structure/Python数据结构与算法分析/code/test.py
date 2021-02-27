num = 125
num &= 0xFFFFFFFF
s = "0123456789abcdef"
mask = 0b1111
print(num & mask)
print(s[num & mask])
