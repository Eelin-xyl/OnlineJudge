line = '4,5,6,7,0,1,2 6'
num = line[line.rfind(' ')+1 : ]
line = line.replace(' ' + num, '') + ','
b = -1
c = 0

for a in range(len(line)):

    if line[a] == ',':
        
        if line[b+1 : a] == num:

            line = c
            break
        
        b = a
        c += 1

if line != c:

    line = -1

print(line)