line = '4,13,5,6,35,85,3'
line += ','
list = []
a = ''
num = 0

for i in line:

    if i == ',':

        list.append(int(a))
        a = ''
    
    else:

        a += i

for m in range(len(list) - 1):

    for n in range(m + 1, len(list)):

        if list[m] + list[n] == 10 or abs(list[m] - list[n]) == 10:

            num += 1
            
print(num)