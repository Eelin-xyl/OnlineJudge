line = '12,13,14,5,6,7,8,9,10'
line += ','
list = []
num = 0

for i in range(len(line)):

    if line[i] == ',':
        list.append(int(line[num : i]))
        num = i + 1

for j in range((len(list)-1)//2):

    list.remove(max(list))
    list.remove(min(list))

print(str(list[0]))