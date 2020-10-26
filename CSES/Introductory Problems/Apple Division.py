n = int(input())
w = input()
w = w.split()
w.sort()
w.reverse()

a = 0
b = 0
for i in w:
    if a >= b:
        b += int(i)
    else:
        a += int(i)

print(abs(a - b))