line = 4626149
a = bin(line).replace('0b', '').zfill(32)
line = ''

for i in range(len(a) - 1, -1, -1):

    line += a[i]

line = int(line, 2)
print(line)