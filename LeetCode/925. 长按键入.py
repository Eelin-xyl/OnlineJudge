name = "alex"
typed = "aaleex"

nm = []
tp = []

last_char = name[0]
count = 0

for c in name:
    if c == last_char:
        count += 1
    else:
        nm.append((last_char, count))
        last_char = c
        count = 1
nm.append((last_char, count))

last_char = typed[0]
count = 0
for c in typed:
    if c == last_char:
        count += 1
    else:
        tp.append((last_char, count))
        last_char = c
        count = 1
tp.append((last_char, count))

if len(nm) != len(tp):
    print(False)

for pair1, pair2 in zip(nm, tp):
    if pair1[0] != pair2[0]:
        print(False)
    
    if pair1[1] > pair2[1]:
        print(False)

print(True)



# for i in range(1, len(name)):
#     if name[i] == name[i - 1]:
#         nm[0][1] += 1
#     else:
#         nm.append(a)
#         nm.append(i)
#         a = 1